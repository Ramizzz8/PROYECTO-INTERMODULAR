from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    ####ESTE ES EL PRIMER BLOQUE####
    cadena = '''
    <!DOCTYPE html>
<html lang="en">
    <head>
        <title>RAMI-BLOG</title>
        <meta charset="UTF-8">
        <style>
            body{background: wheat;color: black;font-family: 'Times New Roman', Times, serif;}
            header,main,footer{background: whitesmoke;padding: 20px; margin: auto ;width: 600px;}
            header,footer{text-align: center;}
            main{color: black;}
        </style>
    </head>
    <body>
        <header><h1>RAMI-BLOG</h1></header>
        <main>
        '''
        #####ESTE ES EL SEGUNDO BLOQUE#######
    archivo = open("blog.json", 'r')
    contenido = json.load(archivo)
    for linea in contenido:
        cadena += '''
            <article>
                <h3>'''+linea['titulo']+'''</h3>
                <time>'''+linea['fecha']+'''</time>
                <p>'''+linea['autor']+'''</p>
                <p>'''+linea['contenido']+'''</p>
            </article>
            '''
            ###ESTE ES EL TERCER BLOQUE ###

    cadena +='''
        </main>
        <footer>(c) Andres Ramirez - Alias Little Dimon</footer>   
    </body>
</html>
'''
    return cadena

#Ahora arranco el servidor


if __name__ == "__main__":
    aplicacion.run(debug=True)