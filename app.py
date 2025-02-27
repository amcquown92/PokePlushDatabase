from flask import Flask, render_template, json, jsonify, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import db_connector as db

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_mcquowna'
app.config['MYSQL_PASSWORD'] = 'LcxdVBnmkrg4' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_mcquowna'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

db_connection = db.connect_to_database
mysql = MySQL(app)
# -------------------- ROUTES -------------------- #

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Customers Page
@app.route('/customers')
def customers():
    return render_template('customers.html')

@app.route('/api/customers', methods=['GET'])
def get_customers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT custID, firstName, lastName, email, address FROM Customers;")
    customers = cur.fetchall()
    cur.close()
    return jsonify(customers)

# Pokémon Plushies Page
@app.route('/pokemon')
def pokemon():
    return render_template('pokemon.html')

@app.route('/api/pokemon', methods=['GET'])
def get_pokemon():
    cur = mysql.connection.cursor()
    cur.execute("SELECT plushieID, plushieName, type AS plushieType, price, stockQty FROM Pokemon;")
    plushies = cur.fetchall()
    cur.close()
    return jsonify(plushies)

# Sales Page
@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/api/sales', methods=['GET'])
def get_sales():
    cur = mysql.connection.cursor()
    cur.execute("SELECT saleID, custID, saleDate FROM Sales;")
    sales = cur.fetchall()
    cur.close()
    return jsonify(sales)

# Sale Items Page
@app.route('/saleItems')
def sale_items():
    return render_template('saleItems.html')

@app.route('/api/saleItems', methods=['GET'])
def get_sale_items():
    cur = mysql.connection.cursor()
    cur.execute("SELECT saleItemID, saleID, plushieID, quantity FROM SaleItems;")
    sale_items = cur.fetchall()
    cur.close()
    return jsonify(sale_items)

# -------------------- RUN APP -------------------- #
if __name__ == "__main__":
    app.run(port=56545, debug=True)