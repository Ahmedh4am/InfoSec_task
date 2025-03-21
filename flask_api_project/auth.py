from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import jwt
import datetime

auth_bp = Blueprint('auth', __name__)
SECRET_KEY = "your_secret_key"

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="security_api"
    )

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data['name']
    username = data['username']
    password = generate_password_hash(data['password'])
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, username, password) VALUES (%s, %s, %s)",
                   (name, username, password))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "User registered successfully!"})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"message": "Invalid credentials"}), 401
    
    token = jwt.encode({
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    }, SECRET_KEY, algorithm="HS256")
    
    return jsonify({"token": token})