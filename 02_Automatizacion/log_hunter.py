# usaremos open(... "r") para abrir el archivo server.log en modo lectura
#y los if para poder filtrar las lineas que tengan errores o ameneza

print("--- iniciando log huhnter, analisis de seguridad---")
# definimos las variables para contar los errores y amenazas

amenazas = 0
fallos = 0
# procedemos abrir el archivo server.log en modo lecura con la funcion open
# usaremos try para manejar las condicionales 
# dentro estara el bloque de open,if y else
try:
    # abrimos en modo lecturar
    with open("server.log","r") as archivo:
        print("leyendo archivo server.log...")

        # recorremos con un bucle cada linea del aarchivo
        for linea in archivo:
            linea = linea.strip()#usamos la funcion strip para limpiar espacios en blanco

            # filtro 1 buscamos Hackers
            if "CRITICAL" in linea:
                print(f"amenaza detectada:{linea}")
                amenazas += 1 #incrmentamos el contador de amenazas en 1
                # filtro 2 buscamos los errores tecnicos
            elif "ERROR" in linea:
                print(f"error tecnico detctado{linea}")
                fallos=1 # incrementamos el contador fallos en 1

     # realizamos el reporte final
    print("-"*20)
    print("Rporte final")
    print(f"amenazas detectadas: {amenazas}")
    print(f"fallos detectados:{fallos}")

    if amenazas > 0:
                    print("alerta, avisar al equipop de ciberseguridad")
    else:
                    print("sistema limpio")
                
                #MANEJAMOS LA EXCEPCION SI EL ARCHIVO NO EXISTE
except FileNotFoundError:
    print("error: el archivo server.log no existe, verificar si fue creado")
