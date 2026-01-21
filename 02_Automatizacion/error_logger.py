#ejercicio de automatizacion EL LOGGER ERROR(SysAdmin)
#vamos a crear un script que simule que el servidor se cayo y nos guarde un reporte de error
#  ----crear un archivo .log
#  ---- nombre de archivo erro_logger.py
# importamos la liberia datetime 

import datetime
# definimos la fecha y hora actuales,usadno datetime
fecha = datetime.datetime.now()

mensaje_error ="[CRITICAL] El servidor de base de datos dejo de responer."
# usaremos "a" (Append) en lugar de "w" para agregar al logsono borrar los anterior 
# aunque esta sea la primera vez, funcionara igual creando el archivo

with open("sistem.log","a")as archivo:
    archivo.write(f"esta es la fecha {fecha} - mensaje de error {mensaje_error}\n")

    print("error ha sido registrado en sistema.log")
    
