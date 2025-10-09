#!/usr/bin/env python3
"""
Task 5: API Security and Authentication Techniques
This module implements both basic HTTP authentication and JWT-based authentication.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuration
# Change this in production
app.config['JWT_SECRET_KEY'] = 'your-secret-string'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# User data with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Basic Authentication
@auth.verify_password
def verify_password(username, password):
    """
    Verify username and password for basic authentication.

    Args:
        username (str): Username
        password (str): Password

    Returns:
        bool: True if credentials are valid, False otherwise
    """
    if username in users and \
            check_password_hash(users[username]['password'], password):
        return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Protected route using basic authentication.

    Returns:
        str: Access granted message
    """
    return "Basic Auth: Access Granted"


# JWT Authentication
@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint that returns JWT token for valid credentials.

    Expected JSON payload:
    {
        "username": "user1",
        "password": "password"
    }

    Returns:
        JSON: Access token or error message
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username in users and check_password_hash(users[username]['password'], password):
        user_data = users[username]
        access_token = create_access_token(identity=username, additional_claims={"role": user_data["role"]})
        return jsonify(access_token=access_token)

    return jsonify({"msg": "Wrong username or password"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Protected route using JWT authentication.

    Returns:
        str: Access granted message
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Protected route that requires admin role.

    Returns:
        str: Access granted message or error
    """
    current_user_id = get_jwt_identity()
    claims = get_jwt()
    user_data = users.get(current_user_id)

    if user_data and user_data.get("role") == "admin":
        return "Admin Access: Granted"

    return jsonify({"error": "Admin access required"}), 403


# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token errors."""
    return jsonify({"msg": "Missing Authorization Header"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token errors."""
    return jsonify({"msg": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle fresh token required errors."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(debug=True)
