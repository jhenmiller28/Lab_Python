import time
import requests
import os

# --- CONFIGURACIÓN SEGURA ---
TOKEN = "8285011702:AAE0Ih5VbKCph-4mhJA7cf6a_sozGYEWr8E"
CHAT_ID = "6598952744"
LOG_PATH = "/var/log/auth.log"

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensaje}
    try:
        requests.post(url, data=payload, timeout=10)
    except Exception as e:
        print(f"❌ Error enviando a Telegram: {e}", flush=True)

# --- LATIDO INICIAL (HEARTBEAT) ---
print("🛡️ [SISTEMA] Centinela 2.0 Iniciando...", flush=True)
enviar_telegram("🚀 ¡Centinela 2.0 en línea! Patrullando logs en AWS...")

# --- BUCLE DE MONITOREO ---
def monitorear():
    print (f"[INFO]Monitoreando {LOG_PATH} en tiempo rel...", flush=True)

    with open(LOG_PATH,"r") as f:
	# ir al final del archivo para no leer ataques pasados
        f.seek(0, 2)

        while True:
            linea = f.readline()
            if not linea:
                time.sleep(0.1) # espear minima de 0.1 segundos para no saturar la cpu del sevirdor
                continue

	    # filtro de seguridad
            if "Failed password" in linea:
                print(f"ATAQUE DETECTADO:{linea.strip()}", flush=True)
                enviar_telegram(f"intento de acceso fallido!\nDetalle:{linea.strip()}")

            elif "Accepted password" in linea:
                enviar_telegram(f"acceso exitoso detectado:\n{linea.strip()}")

if __name__ == "__main__":
    monitorear()

