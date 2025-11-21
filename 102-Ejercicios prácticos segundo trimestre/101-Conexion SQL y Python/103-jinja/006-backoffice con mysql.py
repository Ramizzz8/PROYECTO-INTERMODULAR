from flask import Flask, render_template
import pymysql

conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)

cursor = conexion.cursor()
cursor.execute("SHOW TABLES;")
tablas = []
filas = cursor.fetchall()
for fila in filas:
  tablas.append(fila)

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("backoffice.html", mis_tablas = tablas)

if __name__ == "__main__":
  app.run(debug=True)
