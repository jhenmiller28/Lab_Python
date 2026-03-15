import time
import requests
import os
import re

# colocar nuestra IP publica para que el bot nunca nos bloque el acceso al servidor de aws
MI_IP_SEGURA ="38.172.129.56"

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
print("🛡️ [SISTEMA] Centinela 3.0 con bloqueo de ip..", flush=True)
enviar_telegram("🚀 ¡Centinela3.0 en línea! Patrullando logs en AWS y listo para bloquear ip atacante...")

# --- BUCLE DE MONITOREO ---
def monitorear():
    print (f"CENTINELA MODO DEFENSA ACTIVA...", flush=True)

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
               #aplicamos el molde de regex para poder buscar la ip en linea
                busqueda = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', linea)
             #si el molde encuentra una ip exitosamente...
                if busqueda:
                    ip_atacante = busqueda.group() #extrae el texto limpio
                    #impedimos el bloquearnos a nosotros mismos
                    if ip_atacante == MI_IP_SEGURA:
                        print(f"intento fallido desde ip de confianza({ip_atacante}). Ignorando bloqueo.")
                        continue
                    print(f"ataque detctado. Bloqueadno IP:{ip_atacante}", flush=True)
                   #ataque detectado ,accion de bloque real
                    print (f"-- ATAQUE DETECTADO..IP aislada:{ip_atacante}" , flush=True)
                     # ejecutamos el comando de firawall
                    os.system(f"iptables -A INPUT -s {ip_atacante} -j DROP")
                    enviar_telegram(f"ALERTA DE SGURIDAD \ INTENTO FALLIDO DESDE LA IP :{ip_atacante}")

if __name__ == "__main__":
    monitorear()









