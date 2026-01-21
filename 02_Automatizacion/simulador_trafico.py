#simulador e trafico, crearemos un server.log con 50 lineas de acitvidad
# lass culaes estarn mezcladas con cosas buenas y errores graves

# importamos ramdom para generar datos aleatorios
#imortamos time para manejar fechas y horas

from datetime import datetime
import random
import time

# definimos una lista de posibles eventos,en un directorio de servidor      
eventos = [
    "INFO: Usuario Jhenmiller logueado exitosamente",
    "INFO:Inicio cargado en 0.4 segundos",
    "WARN: Memoria RAM al 80% de uso",
    "ERROR:Base de datos no responde",
    "CRITICAL:Intento de acceso por inyeccion SQL desde la IP 45.23.12.99",
    "INFO: Cierre de sesion de usuario Ethan",
]
# abrimos el archivo server.log en modo escritura para pdoer
# crear los datos simulados
# Crear el archivo server.log 
with open("server.log","w")as f:
    for _ in range (50):
        hora = datetime.now().strftime("%H:%M:%S")
        evento = random.choice(eventos)
        f.write(f"[{hora}] {evento}\n")
print("-"*20)
print("Archivo server.log fue creado con exito ")

