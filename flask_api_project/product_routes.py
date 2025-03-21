from flask import Blueprint, request, jsonify
import mysql.connector
from jwt_middleware import verify_token

product_bp = Blueprint('product', __name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="security_api"
    )

@product_bp.route('/', methods=['POST'])
@verify_token
def add_product(decoded):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (pname, description, price, stock) VALUES (%s, %s, %s, %s)",
                   (data['pname'], data['description'], data['price'], data['stock']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Product added successfully"})