from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL


app = Flask(__name__)

mysql=MySQL()

app.config['MySQL_HOST']='localhost'
app.config['MySQL_PORT']= 3306
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='0806'
app.config['MYSQL_DB']='clientes'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql.init_app(app)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/clientes')
def index_clientes():

 sql='SELECT * FROM datos_clientes'
 conexion=mysql.connection
 cursor=conexion.cursor()
 cursor.execute(sql)
 clientes=cursor.fetchall()
 conexion.commit()
 return render_template('modulos/clientes/index.html', datos_clientes= clientes)

@app.route('/clientes/create')
def create():
   return render_template('modulos/clientes/create.html')

@app.route('/clientes/create/guardar', methods=['POST'])
def clientes_guardar():
   nombre=request.form['nombre']
   telefono=request.form['telefono']
   fecha=request.form['fecha']

   sql='INSERT INTO datos_clientes(nombre, telefono, fecha) VALUES(%s, %s, %s)'
   datos=(nombre, telefono, fecha)
   conexion=mysql.connection
   cursor=conexion.cursor()
   cursor.execute(sql, datos)
   conexion.commit()
   return redirect('/clientes')

if __name__ == '__main__':
    app.run(debug=True)