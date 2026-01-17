import hashlib
passwords_vulnerables = ["123456","jhenmiller_dev", "123456"]
# 1 definimos la SALT  secreto del banco
salt = "xyZ28"

print("--- INICIANDO HASHING CON SALT GLOBAL---")

# BUCLE FOR PARA CADA PASSWORD EN LA LISTA PASSWORDS VULNERABLES
for password in passwords_vulnerables:
    # empezamos el procesood e sazoonado
    # 2 agregamos la salt a la contraeseña "jhenmiller_dev" y se vuelbe "jhenmiller_devxyZ28"
    # definimos la contraseña donde se almacenra la contraseña sazonada
    password_sazonada = password + salt

    # 3 trituramos las contraseñas sazonada
    hash_obj = hashlib.sha256(password_sazonada.encode())
    password_encryp = hash_obj.hexdigest()

    # la manera de leer,interpretar el codigo 
    # a password sazonada se le aplica el meotdo encode para convertir el texto a bytes
    #luego la pasamos como argumento a la fucion sha256 del modulo hashlib
    #el cual creara el objeto hash donde se almacenara el nuevo hash
    # La aplicamos el metodo hexdigest que devuelve una representacion hexadecimal del valor haseado
    # y la guarda en la variable password encryp

    print (f"pass: {password}(+salt) -> hash : {password_encryp}")
    print("_"*40)
