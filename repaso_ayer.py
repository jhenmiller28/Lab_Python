# 1. Variables de entorno(cajas de memoria)
# Python detecta el tipo automaticamente (llamado tipado dinamico)
usuario = "Jhenmiller"  # String (cadena de texto)
ram_gb = 16             #int (entero)
temperatura = 45.5     # float (numero con decimales)
modo_dev = True      # bool (booleano: True o False)

# 2. INPUT (escuhar al usuario)
print("--- INIICIANDO DEAGNOSTICO DEL SISTEMA ---")
#OJO : input siempre CAPTURA TEXTO aunque escribas numeros
estado_energia = input("¿Como esta tu energia hoy (0-100)?:")

# 3. PROCESAMIENTO (operaciones, logica, funciones, etc)
# convertimos el texto ingresado a numero enteropara poder comparar 
energia = int(estado_energia)

if energia >= 70 : 
    mensaje = "¡Modo bestia activado! ¡A programar se ha dicho!"

elif energia >= 40 :
        mensaje = "modo normal, a darle pero con calma"
else :
      mensaje = "alerta, se requiere un cafeecito urgente"

      # 4 OUTPUT (mostrar resultados, HABLAR - F-STRINGS)
      # la F de f-strings significa FORMATEADO, y permite insertar variables dentro del texto usando {}
print("_" * 30 )
print(f"usuario: {usuario} | ram: {ram_gb}gb | temperatura: {temperatura}°c")
print(f"nivel de energia para programar: {mensaje}")
print("_" * 30)
