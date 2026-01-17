# generador.py
import datetime

# Datos Reales del Sistema
hora = datetime.datetime.now()
secreto = "CLAVE_BANCARIA = 123-456-789"

# I/O: Escribir en Disco Duro (Persistencia)
print(f"💾 Creando archivo en disco a las {hora}...")

with open("claves_secretas.txt", "w") as archivo:
    archivo.write(f"REPORTE DEL {hora}\n")
    archivo.write(secreto)

print("✅ Archivo 'claves_secretas.txt' creado exitosamente.")
