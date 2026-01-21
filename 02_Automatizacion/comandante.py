# este script nos aydura a ejecutar comandos basicos de linux
# usaremos la libreria OS Operating System parar interactuar con el sistema operativo

# IMPORTAREMOS LA LIBRERIA OS Y LA LIBRERIA TIME
import os
import time
print("Iniciando protocolo de Comandante de Linux")

# pyhton le dice a liunx" dime quien soy"
print("Ejecutando 'whoami'")
os.system("whoami")
print("-"*20)

# python le dice a linux que  uestre los archivos
print("ejecutandi ls -la")
os.system("ls -la")
print("-"*20)

# python le dice a linux que cree una carpeta nueva
print("Ejecutando 'mkdir carpeta_nueva'")
os.system("mkdir crapeta_fantasma")
print("-"*20)

# usamos time para dar una pausa de 2 segundos,modo dramatico
time.sleep(2) #le damos el parametro de 2 segundos a la funcion sleep de la libreria o modulo time'''

print("-"*20)
print ("eliminando la carpeta fantasma o otras creadas automaticamente")
os.system("rm-rf carpeta_fantasma")

print("protocolo de comandos basicos finalizado")
