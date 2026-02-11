# primero importamos la caja de herramientas
#REQUESTS: es el navegador del robot, asi como usamos chrome/brave
#python usa requests para VER paginass web

#TIME nos permite usar el script SLEEP sin esto se generaria un ataque DDoS
# el robot atacaria el servior millones de veces 

# DATETIME nos da el reloj , en auditoria es escensial saber a que hora paso cada evento
import requests
import time
from datetime import datetime

#configuracion de variables
#aquidefinimos las reglas de que se vigila y cada que tiempo
#URL_OBEJTIVO LA DIRECCION DE LA CASA
#INTERVALO CADA CUANTO TIEMPO PASA EL CENTINELA
URL_OBJETIVO = "https://www.google.com"
INTERVALO = 5

#FUNCION PRINCIPAL DEDL CEREBRO
#DEFINIMOS la accion principal del cerebro
# lo primero que hara es mirar el reloj y registrarlo
#la funcion revisar_servidor():
def revisar_servidor():
    ahora = datetime.now().strftime('%H:%M:%S')

# LA RED DE SEGURIDAD,NUNCA ASUMIMOS QUE TODooo SALDRA BEIN
# TRY: (INTENTA HACER ESTO...)
# EXECPT (SI ALGO EXPLOTA NO TE MUERAS, HAZ ESTO OTRO)
    try:
        respuesta= requests.get(URL_OBJETIVO,timeout=5)
# REQUESTS.GET el robot envia una señal al servidor 
#TIMEOUT=5 si el servidor no responde en 5 segundos el robot lo marca como error
#no se queda espeadno para siempre

##la decision if/else
#en lenguaje http codigo 200 todo esta bien
#si es 404 es no encontrado o 500 no existe
        if respuesta.status_code ==200:
             print(f"[{ahora}online]")
        else:
            print(f"[{ahora}] alerta | codigo:{respuesta.status_code}")

#  el manejo de errores
# si el servidor esta apagado o no hay internet, el codigo de arriba fallaria
# este bloque atrapa ese error y te avisa""el servidoe esta caido"
    except requests.exceptions.ConnectionError:
        print (f"[{ahora}] caido | nos e puede conectar...")

#el bucle infinito devigilancia
#whilr true es un bucle que no termina hasta qye se apague la pc o lo detengamos
#time.sleep pra que el robbot trabaje y descanse 5 segundos y seuga asi
#keyboardInterrupt es para que podamos salir con control c y no salgag error
try: 
    while True:                #haz esto por siempre
            revisar_servidor()    #ejecuta la funcion de arriba
            time.sleep(INTERVALO) #duerme 5 segundos
except KeyboardInterrupt:
    print("vigilancia detenida")
