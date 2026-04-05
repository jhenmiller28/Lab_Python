import os
import re
import time
import psycopg2

# CONFIGURACION BASICA PARA EL MONITOREO DE LOGS Y BLOQUEO DE IPS SOSPECHOSAS
LOG_PATH = "/var/log/auth.log"
MI_IP_SEGURA = "TU_IP_DE_ATE"  # ACA IRA LA IP SEGURA


def enviar_telegram(mensaje):
    # ACA IRA LA LOGICA DEL BOT DE TELEGRAM, PERO POR AHORA SOLO ENVIAMOS MENSAJES
    print(f" [TELEGRAM]: {mensaje}")
    print(
        f"mensaje de prueba con implementacion de github actions para despliegue continuo en AWS EC2"
    )


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
            host="localhost",  # Usamos localhost porque el contenedor está en modo host
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )
    except Exception as e:
        print(f"❌ Error fatal: No se pudo conectar a la DB: {e}")
        return

    # LECTURA DE LOGS (INTENTOS DE INGRESO)EN TIEMPO REAL Y APLICACION DE FILTROS DE SEGURIDAD PARA DETECTAR IPS SOSPECHOSAS Y BLOQUEARLAS
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
                if "Failed password" in linea:
                    # Buscamos la IP con Regex
                    busqueda = re.search(r"(\d{1,3}\.){3}\d{1,3}", linea)

                    if busqueda:
                        ip_atacante = busqueda.group()

                        # FILTRO DE CONFIANZA CON LA WHITE LIST(MI IP SEGURA)
                        if ip_atacante == MI_IP_SEGURA:
                            print(
                                f" Intento fallido desde IP segura ({ip_atacante}). Ignorando."
                            )
                            continue

                        # LOGICA DE STRIKES PARA BLOQUEAR IPS QUE INTENTEN
                        # INGRESAR Y DE FAILED PASSWORD
                        strikes = registrar_y_obtener_intentos(conn, ip_atacante)

                        if strikes == 1:
                            msg = f" STRIKE 1: IP {ip_atacante} detectada. Registro guardado."
                            print(msg)
                            enviar_telegram(msg)

                        elif strikes == 2:
                            msg = (
                                f" BLOQUEO: IP {ip_atacante} baneada por reincidencia."
                            )
                            print(msg)
                            # COMANDO PARA BLOQUEAR EN FIREWALL AWS/    UBUNTU
                            os.system(
                                f"sudo iptables -A INPUT -s {ip_atacante} -j DROP"
                            )
                            enviar_telegram(msg)

                        elif strikes > 2:
                            # SI TIENE DOS STRIKES O MAS,
                            #  YA ESTA BLOQUEADA,
                            pass

    except FileNotFoundError:
        print(f"----Error: No se encontró el archivo en {LOG_PATH}")
    except KeyboardInterrupt:
        print("\n----- Centinela desactivado por el usuario.")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    monitorear()
