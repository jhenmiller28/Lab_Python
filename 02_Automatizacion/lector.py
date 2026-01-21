# este script leera el archivo txt que fue generado
# previamente po el codigo generador.py

# lector.py
print("---Leyendo las claves secretas ---")

try:
    # "r" = Read (Solo lectura, no borra nada,no modifica nada)
    with open("claves_secretas.txt", "r") as archivo:
        contenido = archivo.read() # extre todo el texto hacia la RAM
        
        print("Contenido descifrado:")
        print(contenido)

except FileNotFoundError:
    print("❌ ERROR: El archivo no existe. Ejecuta primero el generador.")

print("--- FIN DE LA LECTURA ---")