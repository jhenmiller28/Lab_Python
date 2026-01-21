#en este validador de passwords usaremos la funcion len()
#para poder contar el tamaño de la password
#Simula que revisas si las contraseñas de los usuarios cumplen el largo mínimo.


#EMPEZAMOS CON LA LISTA DE PASSWORD

passwords = ["12345","jhenmiller28","abcd","chilaquiles"]
#recordemos que las contraseñas y lo qu se ingresa por teclado es considerado texto en python
# por eso el uso de las comillas en las lista de password
print("--- validando (AUDITORIA)el tamaño de las contraseñas para ver si son seuguras---")

for password in passwords:
    if len(password)<8:
        print(f"contraseña debil {len(password)} nr de caracteres en: {password}")
    else:
        print (f"contraseña segura {len(password)}nr de caracteres en:{password}")
