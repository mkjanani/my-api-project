from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection Config
db = mysql.connector.connect(
    host="mysql.railway.internal",  # Replace with Railway Host
    user="root",      # Replace with Railway Username
    password="bGPugPpRxIYqaLDbpfnQeKTrKiKgDNft",  # Replace with Railway Password
    database="railway",  # Replace with Railway Database Name
    port=3306
)

cursor = db.cursor(dictionary=True)

# API to fetch all vendors
@app.route('/vendors', methods=['GET'])
def get_vendors():
    cursor.execute("SELECT * FROM vendors")  # Change "vendors" to your table name
    vendors = cursor.fetchall()
    return jsonify(vendors)

# API to fetch a specific vendor by ID
@app.route('/vendor/<int:vendor_id>', methods=['GET'])
def get_vendor(vendor_id):
    cursor.execute("SELECT * FROM vendors WHERE id = %s", (vendor_id,))
    vendor = cursor.fetchone()
    if vendor:
        return jsonify(vendor)
    return jsonify({"error": "Vendor not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



