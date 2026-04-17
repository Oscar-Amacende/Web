#Lib para servidor
from flask import Flask, jsonify, render_template
#Sqlite para base de datos
import sqlite3
from datetime import datetime
import click


#Nombre de la app
app = Flask(__name__) 

#Enrutado dinámico index
@app.route('/') 
def landing(): 
    return "Holas" 

if __name__ == '__main__':
    app.run(debug=True)
