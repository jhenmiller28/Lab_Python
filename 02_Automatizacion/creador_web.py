# con python podemos eescribir HTML 
# crearemos una pag web con python
titulo = "Mi portafolio DevOps"
mensaje = "Hola, soy Jhenmiller y este es un sitio creado automaticamente con python"

html_code = f"""
<html>
    <head>
        <title>{titulo}</title>
    </head>
    <body>
        <h1>{titulo}</h1>
        <p>{mensaje}</p>
        <hr> 
        <p><i>generado por sripts de automatizacion en python</i></p>
    </body>
</html>
""" 
with open ("index.html","w")as web:
    web.write(html_code)
    print("pagina web creada con python. 'index.html'abrela en tu navegador de prefenrecia")
