from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  return '''
    <!doctype html>
    <html>
      <head>
        <title>Prueba de HTML con Flask</title>
        <style>
          body {background-color: lightblue;}
          h1 {color: white; text-align: center;}
          p {font-family: verdana, sans-serif;}
        </style>
      </head>
      <body>
        <h1>Bienvenido a mi sitio web</h1>
        <p>Este es un ejemplo de HTML con Flask.</p>
        <img src="https://example.com/image.jpg" alt="Ejemplo">
      </body>
    </html>
  '''
@aplicacion.route("/hola/<nombre>")
def hola(nombre):
  return f"Hola, {nombre}!"

if __name__ == "__main__":
  aplicacion.run(debug=True)
