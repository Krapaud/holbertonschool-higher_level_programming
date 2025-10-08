#!/usr/bin/env python3
"""
Task 4: Develop a Simple API using Python with Flask
This module creates a Flask API with various endpoints for user management.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
# Structure: {username: {user_data}}
# Example: {"jane": {"username": "jane", "name": "Jane", "age": 28,
#           "city": "Los Angeles"}}
users = {}


@app.route('/')
def home():
    """
    Root endpoint that returns a welcome message.

    Returns:
        str: Welcome message
    """
    # TODO: Return welcome message
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """
    Returns a list of all usernames stored in the API.

    Returns:
        JSON: List of usernames
    """
    # Return list of all usernames from users dictionary
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """
    Returns the API status.

    Returns:
        str: Status message
    """
    # Return "OK" status
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Returns the full user object for the given username.

    Args:
        username (str): The username to look up

    Returns:
        JSON: User object or error message
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the users dictionary.

    Expected JSON payload:
    {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    Returns:
        JSON: Confirmation message with user data or error
    """
    data = request.get_json()

    # Check if username is provided
    if not data or not data.get("username"):
        return jsonify({"error": "Username is required"}), 400

    username = data.get("username")

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    # Add the new user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__": app.run()
