from flask import Flask, request, jsonify
from appwrite.client import Client
from appwrite.services.account import Account
import os

app = Flask(__name__)

# Initialize Appwrite Client
client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')  # Appwrite Base URL
client.set_project('6765e2280022c08ed121')  # Your Project ID
client.set_key('standard_a33daf76dd1ac64a8dffac5ecc7b7572f669114e140df3af6add28391712ea5a9e6c0d29476b5aaf07c604e43aecfaa133a2a919a46c73b965545609004e973a164c4aae1d0be3a9707bb9ca1a085e9afe61b1d047abc7ff3a0a9ca705fb68e100535fe55fe17286c2a3367c90c3d0c033857d0c79b524094bd5b829bb5e7570')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    account = Account(client)

    try:
        session = account.create_session(email=email, password=password)
        return jsonify({"message": "Login successful", "session": session}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    account = Account(client)

    try:
        user = account.create(email=email, password=password, name=name)
        return jsonify({"message": "Signup successful", "user": user}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable or default to 5000
    app.run(host='0.0.0.0', port=port, debug=False)  # Disable debug for production
