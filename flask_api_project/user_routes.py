from flask import Blueprint, request, jsonify
import mysql.connector
from jwt_middleware import verify_token

user_bp = Blueprint('user', __name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="security_api"
    )

@user_bp.route('/<int:id>', methods=['PUT'])
@verify_token
def update_user(decoded, id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s WHERE id=%s", (data['name'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User updated successfully"})