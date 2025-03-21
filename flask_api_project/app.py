from flask import Flask
from auth import auth_bp
from user_routes import user_bp
from product_routes import product_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(product_bp, url_prefix='/products')

@app.route('/')
def home():
    return "Welcome to the Flask API!"

if __name__ == '__main__':
    app.run(debug=True)