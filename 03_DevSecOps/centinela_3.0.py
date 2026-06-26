import os
import re
import time
import psycopg2
import requests
from dotenv import load_dotenv  # <-- PASO 1: Importamos la librería

# CONFIGURACION BASICA PARA EL MONITOREO DE LOGS Y BLOQUEO DE IPS SOSPECHOSAS
LOG_PATH = "/var/log/auth.log"

# ¡ESTA ES LA MAGIA! Carga el archivo .env antes de cualquier os.getenv
load_dotenv()  # <-- PASO 2: Inyectamos los secretos en la memoria de Python

# Cargamos la IP de confianza desde el entorno (.env)
MI_IP_SEGURA = os.getenv("MI_IP_SEGURA")  # Ahora sí tendrá: 100.106.191.78


def enviar_telegram(mensaje):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("⚠️ [TELEGRAM] Error: Faltan credenciales en el .env")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"}

    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            print("🚀 [TELEGRAM] ¡Alerta de strike enviada en vivo al celular!")
        else:
            print(f"❌ [TELEGRAM] Error de API. Código: {response.status_code}")
    except Exception as e:
        print(f"❌ [TELEGRAM] Excepción de red: {e}")


def registrar_y_obtener_intentos(conn, ip):
    try:
        cur = conn.cursor()
        # USAMOS UPSERT PARA PODER REGISTRAR EL PRIMER INTENTO U ACTUALIZAR LOS SIGUIENTES DE MANERA EFICIENTE
        query = """
        INSERT INTO ataques (ip, intentos, ultimo_ataque)
        VALUES (%s, 1, CURRENT_TIMESTAMP)
        ON CONFLICT (ip) 
        DO UPDATE SET intentos = ataques.intentos + 1, ultimo_ataque = CURRENT_TIMESTAMP
        RETURNING intentos;
        """
        cur.execute(query, (ip,))
        intentos = cur.fetchone()[0]
        conn.commit()
        cur.close()
        return intentos
    except Exception as e:
        print(f" Error de DB: {e}")
        conn.rollback()
        return 1


def monitorear():
    print(" [SISTEMA] Centinela 3.0 con bloqueo de IP iniciado..")
    print("CENTINELA MODO DEFENSA ACTIVA...", flush=True)

    # CONEXION A LA BASE DE DATOS POSTEGRESQL
    try:
        conn = psycopg2.connect(
            host="127.0.0.1",  # mapeado en los puertos de Docker
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),  # Ahora sí jalará el "123"
        )
        enviar_telegram(
            "🚀 *Centinela 3.0 iniciado:* Monitoreo activo y patrullando el puerto 22 en AWS EC2."
        )

    except Exception as e:
        print(f"❌ Error fatal: No se pudo conectar a la DB: {e}")
        return

    # LECTURA DE LOGS (INTENTOS DE INGRESO) EN TIEMPO REAL
    try:
        with open(LOG_PATH, "r") as f:
            # VAMOS AL FINAL DEL ARCHIVO PARA SOLO LEER LOS NUEVOS INTENTOS DE INGRESO
            f.seek(0, 2)

            while True:
                linea = f.readline()
                if not linea:
                    time.sleep(0.1)
                    continue

                # EL FILTRO DE SEGURIDAD QUE NOS AYUDARA A DETECTAR IPS SOSPECHOSAS
                if any(
                    keyword in linea
                    for keyword in [
                        "Failed password",
                        "Connection closed",
                        "Connection reset",
                        "Invalid user",
                        "Disconnected",
                    ]
                ):
                    # 1. Buscamos la IP con Regex
                    busqueda = re.search(r"(\d{1,3}\.){3}\d{1,3}", linea)

                    if busqueda:
                        ip_atacante = busqueda.group()

                        # --- INICIO DE LA WHITELIST ---
                        if ip_atacante == MI_IP_SEGURA:
                            print(
                                f"✅ Acceso detectado desde IP segura ({ip_atacante}). Ignorando reglas de bloqueo."
                            )
                            continue
                        # --- FIN DE LA WHITELIST ---

                        # LOGICA DE STRIKES
                        strikes = registrar_y_obtener_intentos(conn, ip_atacante)

                        if strikes == 1:
                            msg = f"🟡 STRIKE 1: IP {ip_atacante} detectada. Registro guardado."
                            print(msg)
                            enviar_telegram(msg)

                        elif strikes == 2:
                            msg = f"🔴 BLOQUEO: IP {ip_atacante} baneada por reincidencia."
                            print(msg)
                            os.system(
                                f"sudo iptables -A INPUT -s {ip_atacante} -j DROP"
                            )
                            enviar_telegram(msg)

                        elif strikes > 2:
                            pass  # Ya está bloqueada, no hacemos nada adicional

    except FileNotFoundError:
        print(f"----Error: No se encontró el archivo en {LOG_PATH}")
    except KeyboardInterrupt:
        print("\n----- Centinela desactivado por el usuario.")
    finally:
        # Verificación de cierre seguro de conexión
        if "conn" in locals() and conn:
            conn.close()


if __name__ == "__main__":
    monitorear()
