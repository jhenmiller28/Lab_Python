#en una lista de puertos de red, el script debe decirnos 
#qe servicios son
# usaremos if,elif,else
#Objetivo: Entrenar el cerebro para filtrar datos y tomar decisiones.

#EMPEZAMOS LA LISTA DE PUERTOS
puertos = [22,80,443,8080,3306]

# recorremos lalista de puertos,antes dejamos un mensjae con
print("--- ANALAIZAZNDO LOS PUERTOS EN LA LISTA----")

# PARA PUERTO EN LA LISTA PUERTOS RECORREMOS 
for puerto in puertos:
    if puerto == 22:
        print (f"el puerto{puerto}:es ssh(acceso remoto seguro) - critico")
    elif puerto == 80 or puerto == 443:
        print (f"el puerto {puerto}: es de la web (HTTP/HTTPS)") 
    elif puerto == 3306:
        print (f"el puerto{puerto}es de la base de datos MySql")
    else :
        print (f"el puerto{puerto} es desconocido")