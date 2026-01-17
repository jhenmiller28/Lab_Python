# scanner.py
# Simulación de datos en memoria (RAM)
archivos = ["foto.jpg", "tesis.doc", "meme.png", "factura.pdf", "virus.exe"]

print("--- 🔍 INICIANDO ESCANEO (RAM) ---")

for archivo in archivos:
    if ".pdf" in archivo or ".doc" in archivo:
        print("✅ IMPORTANTE: " + archivo)
    else:
        print("🗑️ Basura: " + archivo)

print("--- 🏁 FIN ---")
