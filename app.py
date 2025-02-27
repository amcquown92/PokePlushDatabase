from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_mcquowna'
app.config['MYSQL_PASSWORD'] = 'LcxdVBnmkrg4' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_mcquowna'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)


# Routes
@app.route('/')
def index():
    # query = "SELECT * FROM diagnostic;"
    # query1 = 'DROP TABLE IF EXISTS diagnostic;'
    # query2 = 'CREATE TABLE diagnostic(id INT PRIMARY KEY AUTO_INCREMENT, text VARCHAR(255) NOT NULL);'
    # query3 = 'INSERT INTO diagnostic (text) VALUES ("MySQL is working for yourONID!");'
    # query4 = 'SELECT * FROM diagnostic;'
    # cur = mysql.connection.cursor()
    # cur.execute(query1)
    # cur.execute(query2)
    # cur.execute(query3)
    # cur.execute(query4)
    # results = cur.fetchall()

    # return "<h1>MySQL Results</h1>" + str(results[0])
    return render_template('index.j2')

@app.route('/customers')
def customers():
    return render_template('customers.j2')

@app.route('/pokemon')
def pokemon():
    return render_template('pokemon.j2')

@app.route('/sales')
def sales():
    return render_template('sales.j2')

@app.route('/sale_items')
def sale_items():
    return render_template('sale_items.j2')


# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=56544, debug=True)