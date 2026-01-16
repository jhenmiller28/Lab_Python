import hashlib
# 1 lista de datos vulnerables(de la verguenza)
# [] una lista, array permite guardar varios multiples variables o elementos
# crear la lista de contraseñas vulnerables
#las contraseñas aunque tengan nuemros, deben ir enre comillas dobles o simples
passwords_inseguras = ["jhenmiller_dev","admin123", "jhenmiller2026", "banco_seguro", "123456"]

print ("--- INICIANDO EL PROTOCOLO DE HASHING MASIVO---")
# 2 EL BUCLE FOR
# TRADUCIDO A LENGUA HUMANA:
# PARA CADA elemento EN LA LISTA DE CONTRASEÑAS INSEGURAS
for password in passwords_inseguras:
    # 3 el proceso de hashing, la trituradora de datos
    # convertimos el texto de la lista en bytes con (.encode)y luego
    # LO HASHEAMOS CON SHA256
    hash_obj = hashlib.sha256(password.encode())
    password_triturada = hash_obj.hexdigest()
    # aqui se tritura las contraseñas dentro de la lista contraseñas inseguras

    # 4 IMPRIMIR EL RESULTADO
    print(f"contraseña original:{password} >>> contraseña hasheada :{password_triturada}")

    print("-"*40)
    print("--- HASHING DE CONTRASEÑAS VULNERABLES COMPLETADO!!! ---")