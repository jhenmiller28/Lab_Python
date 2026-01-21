# generador de configuracion DevOps
# muchos programas usan archivos .ini o .conf y vamos a crear unp automaticamente
# escribirimos multiples lineas estructuradas


print ("--- GENERANDO ARCHIVOS DE CONIGURACION INICIAL ---")

info_bd = "host=localhost\nuser=root\nport=3306"
info_App = "debug = true\inversion = 1.0.0"

with open ("config.ini","w") as config:
    config.write("[database]\n")
    config.write(info_bd + "\n\n") #doble salto de linea para separar secciones
    config.write("\n[app]\n")
    config.write(info_App + "\n")
    print ("Archivo 'config.ini' ya esta listo para usarse " )            