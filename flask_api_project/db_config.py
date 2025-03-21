import mysql.connector

# Establish database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="security_api"
)
cursor = conn.cursor()

# Create Users Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(256) NOT NULL
)
''')

# Create Products Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    pid INT AUTO_INCREMENT PRIMARY KEY,
    pname VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
cursor.close()
conn.close()

print("Database and tables created successfully!")