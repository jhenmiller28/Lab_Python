import requests
import time
import os

# --- 1. CONFIGURACIÓN (Tus credenciales) ---
TOKEN_TELEGRAM = "6821389279:AAF8O7QjGz1_v_Y3Nn9P2D7N4xM7S_W4Cok"
CHAT_ID = "6598952744"
URL_A_VIGILAR = "https://www.gooOgle.com"  # ¡Con comillas!
INTERVALO = 60

# --- 2. FUNCIONES DE TRABAJO ---

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensaje}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error enviando a Telegram: {e}")

def revisar_servidor():
    try:
        # Aquí usamos la variable que tiene las comillas
        respuesta = requests.get(URL_A_VIGILAR, timeout=10)
        if respuesta.status_code == 200:
            print(f"[{time.ctime()}] El servidor {URL_A_VIGILAR} está UP.")
        else:
            enviar_telegram(f"⚠️ Alerta: El servidor devolvió código {respuesta.status_code}")
    except Exception as e:
        enviar_telegram(f"🚨 CRÍTICO: No se puede acceder a la URL. Error: {e}")

def vigilar_intrusos():
    archivo_log = "/var/log/auth.log"
    comando = f"tail -n 1 {archivo_log}"
    try:
        with os.popen(comando) as f:
            linea = f.read()
            if "Failed password" in linea:
                msg = f"🔒 SEGURIDAD: Intento de acceso fallido detectado!\nDetalle: {linea.strip()}"
                enviar_telegram(msg)
    except Exception as e:
        print(f"Error leyendo logs: {e}")

# --- 3. EJECUCIÓN PRINCIPAL ---

if __name__ == "__main__":
    enviar_telegram("🚀 Centinela DevSecOps Activo y Patrullando")
    print("--- Iniciando patrullaje ---")
    
    while True:
        revisar_servidor()
        vigilar_intrusos()
        time.sleep(INTERVALO)
