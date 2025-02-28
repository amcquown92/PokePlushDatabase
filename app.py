from flask import Flask, render_template, request, redirect, jsonify
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

@app.route('/saleItems')
def sale_items():
    return render_template('saleItems.html')

# -------------------- CRUD API ENDPOINTS -------------------- #

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
@app.route('/api/pokemon', methods=['GET'])
def get_pokemon():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT plushieID, plushieName, type, price, stockQty FROM Pokemon;")
        plushies = cur.fetchall()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
    return jsonify(plushies)

@app.route('/api/pokemon', methods=['POST'])
def add_pokemon():
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Pokemon (plushieName, type, price, stockQty) VALUES (%s, %s, %s, %s)",
                    (data['plushieName'], data['type'], data['price'], data['stockQty']))
        mysql.connection.commit()
        return jsonify({"message": "Pokémon plushie added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

@app.route('/api/pokemon/<int:plushieID>', methods=['PUT'])
def update_pokemon(plushieID):
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Pokemon SET plushieName=%s, type=%s, price=%s, stockQty=%s WHERE plushieID=%s",
                    (data['plushieName'], data['type'], data['price'], data['stockQty'], plushieID))
        mysql.connection.commit()
        return jsonify({"message": "Pokémon plushie updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

@app.route('/api/pokemon/<int:plushieID>', methods=['DELETE'])
def delete_pokemon(plushieID):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Pokemon WHERE plushieID=%s", (plushieID,))
        mysql.connection.commit()
        return jsonify({"message": "Pokémon plushie deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

# -------------------- RUN APP -------------------- #
if __name__ == "__main__":
    app.run(port=56543, debug=True)
