# Citation for this file:
# Date: 03/15/2025
# Adapted from: Flask Starter App - BSG People App
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app/tree/master/bsg_people_app
# Type: Source Code
# Notes: We used this guide to Flask as a reference for providing structure for App file and help running Flask and Gunicorn, but wrote our own code.from flask import Flask, render_template, request, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database Configuration
app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_resili'
app.config['MYSQL_PASSWORD'] = '5447'  # last 4 of ONID
app.config['MYSQL_DB'] = 'cs340_resili'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# -------------------- HTML Pages -------------------- #

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers')
def customers():
    return render_template('customers.html')

@app.route('/pokemon')
def pokemon():
    return render_template('pokemon.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/saleitems')
def sale_items():
    return render_template('saleitems.html')

# -------------------- Customers Entity CRUD -------------------- #

# READ Customers
@app.route('/api/customers', methods=['GET'])
def get_customers():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT custID, firstName, lastName, email, address FROM Customers;")
        customers = cur.fetchall()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
    return jsonify(customers)

# CREATE a New Customer
@app.route('/api/customers', methods=['POST'])
def add_customer():
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Customers (firstName, lastName, email, address) VALUES (%s, %s, %s, %s)",
                    (data['firstName'], data['lastName'], data['email'], data.get('address', None)))
        mysql.connection.commit()
        return jsonify({"message": "Customer added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# UPDATE a Customer
@app.route('/api/customers/<int:custID>', methods=['PUT'])
def update_customer(custID):
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Customers SET firstName=%s, lastName=%s, email=%s, address=%s WHERE custID=%s",
                    (data['firstName'], data['lastName'], data['email'], data.get('address', None), custID))
        mysql.connection.commit()
        return jsonify({"message": "Customer updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# DELETE a Customer
@app.route('/api/customers/<int:custID>', methods=['DELETE'])
def delete_customer(custID):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Customers WHERE custID=%s", (custID,))
        mysql.connection.commit()
        return jsonify({"message": "Customer deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# -------------------- Pokemon Entity CRUD -------------------- #

# READ Pokemon
@app.route('/api/pokemon', methods=['GET'])
def get_pokemon():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT plushieID, plushieName, plushieType, price, stockQty FROM Pokemon;")
        plushies = cur.fetchall()
    except Exception as e:
        print("Error in get /api/pokemon:", e)
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
    return jsonify(plushies)

# CREATE new Pokemon
@app.route('/api/pokemon', methods=['POST'])
def add_pokemon():
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Pokemon (plushieName, plushieType, price, stockQty) VALUES (%s, %s, %s, %s)",
                    (data['plushieName'], data['plushieType'], data['price'], data['stockQty']))
        mysql.connection.commit()
        return jsonify({"message": "Pokemon plushie added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()

# UPDATE a Pokemon
@app.route('/api/pokemon/<int:plushieID>', methods=['PUT'])
def update_pokemon(plushieID):
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Pokemon SET plushieName=%s, plushieType=%s, price=%s, stockQty=%s WHERE plushieID=%s",
                    (data['plushieName'], data['plushieType'], data['price'], data['stockQty'], plushieID))
        mysql.connection.commit()
        return jsonify({"message": "Pokémon plushie updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()

# Delete a Pokemon
@app.route('/api/pokemon/<int:plushieID>', methods=['DELETE'])
def delete_pokemon(plushieID):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Pokemon WHERE plushieID=%s", (plushieID,))
        mysql.connection.commit()
        return jsonify({"message": "Pokemon plushie deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()

# -------------------- Sales Entity CRUD -------------------- #

# READ Sales
@app.route('/api/sales', methods=['GET'])
def get_sales():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT saleID, custID, saleDate FROM Sales;")
        sales = cur.fetchall()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
    return jsonify(sales)

# CREATE a Sale
@app.route('/api/sales', methods=['POST'])
def add_sales():
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Sales (custID, saleDate) VALUES (%s, %s)",
                    (data['custID'], data['saleDate']))
        mysql.connection.commit()
        return jsonify({"message": "Sale added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# UPDATE a Sale
@app.route('/api/sales/<int:saleID>', methods=['PUT'])
def update_sale(saleID):
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Sales SET custID=%s, saleDate=%s WHERE saleID=%s",
                    (data['custID'], data['saleDate'], saleID))
        mysql.connection.commit()
        return jsonify({"message": "Sale updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# DELETE a Sale
@app.route('/api/sales/<int:saleID>', methods=['DELETE'])
def delete_sale(saleID):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Sales WHERE saleID=%s", (saleID,))
        mysql.connection.commit()
        return jsonify({"message": "Sale deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# -------------------- SaleItems Entity CRUD -------------------- #

# READ SaleItems
@app.route('/api/saleitems', methods=['GET'])
def get_saleitems():
    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT SaleItems.saleItemID, Sales.saleID, Pokemon.plushieName, SaleItems.quantity 
            FROM SaleItems 
            INNER JOIN Sales ON SaleItems.saleID = Sales.saleID 
            INNER JOIN Pokemon ON SaleItems.plushieID = Pokemon.plushieID;
        """)
        saleItems = cur.fetchall()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
    return jsonify(saleItems)

# CREATE a SaleItem
@app.route('/api/saleitems', methods=['POST'])
def add_saleitem():
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO SaleItems (saleID, plushieID, quantity) VALUES (%s, %s, %s)",
                     (data['saleID'], data['plushieID'], data['quantity']))
        mysql.connection.commit()
        return jsonify({"message": "SaleItem added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# UPDATE a SaleItem
@app.route('/api/saleitems/<int:saleItemID>', methods=['PUT'])
def update_saleItem(saleItemID):
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("UPDATE SaleItems SET saleID=%s, plushieID=%s, quantity=%s WHERE saleItemID=%s",
                    (data['saleID'], data['plushieID'], data['quantity'], saleItemID))
        mysql.connection.commit()
        return jsonify({"message": "SaleItem updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# DELETE a SaleItem
@app.route('/api/saleitems/<int:saleItemID>', methods=['DELETE'])
def delete_saleItem(saleItemID):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM SaleItems WHERE saleItemID=%s", (saleItemID,))
        mysql.connection.commit()
        return jsonify({"message": "SaleItem deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()


# -------------------- RUN APP -------------------- #
if __name__ == "__main__":
    app.run(port=56545, debug=True)
