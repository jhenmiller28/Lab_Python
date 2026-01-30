import requests  # Librería externapara hacer peticiones HTTP (como un navegador sin pantalla)
import time      # Librería estándar para manejar pausas y medir tiempos, si vinen con python

# Se usan MAYÚSCULAS para indicar que son valores fijos que no cambian durante la ejecución.

SITIOS = ["https://www.google.com", "https://www.github.com", "http://sitio-falso-que-no-existe.com"]

INTERVALO = 5  # Tiempo de espera (en segundos) entre cada ciclo de revisión

def revisar_sitios():
    """
    definimos la función principal que monitorea una lista de sitios web.
    
    Funcionalidad:
    1. Entra en un bucle infinito.
    2. Itera sobre cada URL en la lista previamente declarda SITIOS.
    3. Intenta conectarse y mide el tiempo de respuesta.
    4. Maneja errores comunes como (caída, lentitud).
    
    No recibe parámetros ni retorna valores (corre para siempre).
    """
    
    print(f"🕵️  Iniciando Monitor de Red... (Presiona Ctrl+C para detener)\n")
    
    # BLOQUE 1: El Bucle Infinito
    # 'while True' asegura que el programa nunca termine por sí solo.
    # Es esencial para programas demonios(Daemons), servicios o monitores continuos.
    while True:
        
        # BLOQUE 2: Iteración
        # Recorremos la lista 'SITIOS' uno por uno.
        for sitio in SITIOS:
            
            # BLOQUE 3: Manejo de Errores (El "Airbag")
            # 'try' intenta ejecutar el código peligroso. Si falla, salta al 'except'.
            try:
                # Capturamos el tiempo exacto antes de la petición
                inicio = time.time()
                
                # --- LÍNEA CRÍTICA ---
                # timeout=3: Si el servidor no responde en 3 seg, corta la llamada.
                # Sin esto, el script podría quedarse colgado eternamente.
                respuesta = requests.get(sitio, timeout=3)
                
                # Calculamos cuánto tardó (Tiempo actual - Tiempo inicio)
                tiempo_total = time.time() - inicio
                
                # Verificamos el Código de Estado HTTP
                # 200 = OK (Éxito). Cualquier otro número suele ser un problema o redirección.
                if respuesta.status_code == 200:
                    # Usamos f-strings (f"...") para insertar variables dentro del texto
                    print(f" [OK] {sitio} - Respondió en {tiempo_total:.2f}s")
                else:
                    print(f" [WARN] {sitio} - Código extraño: {respuesta.status_code}")
            
            # BLOQUE 4: Excepciones Específicas
            # Si 'requests' lanza un error de conexión (DNS, cable desconectado, etc.)
            except requests.exceptions.ConnectionError:
                print(f" [DOWN] {sitio} - No se pudo conectar (Servidor caído o URL mal escrita,o sin conexion).")
            
            # Si el servidor acepta la conexión pero tarda más de 3 segundos (timeout)
            except requests.exceptions.Timeout:
                print(f" [SLOW] {sitio} - muy Lento: Se agotó el tiempo de espera.")
            
            # 'Exception' es el comodín: atrapa cualquier otro error no previsto.
            except Exception as error_desconocido:
                print(f"💥 [ERROR] {sitio} - Error inesperado,averigualo: {error_desconocido}")

        # BLOQUE 5: El Descanso
        # Es vital dormir el script para no saturar tu CPU ni bloquear tu red.
        print("-" * 30)
        time.sleep(INTERVALO)

# Punto de entrada del script
# Esta condición verifica si el archivo se está ejecutando directamente.
if __name__ == "__main__":
    try:
        revisar_sitios()
    # Captura cuando el usuario presiona Ctrl + C en la terminal
    except KeyboardInterrupt:
        print("\n🛑 Monitoreo detenido manualmente. ¡nos vemos luego!")