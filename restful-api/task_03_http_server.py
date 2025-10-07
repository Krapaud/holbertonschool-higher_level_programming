#!/usr/bin/env python3
"""
Task 3: Develop a simple API using Python with the `http.server` module

Background:
The http.server module in Python's standard library provides basic classes
for implementing web servers. While it's not typically used for production
applications, it's a handy tool for building simple web servers and
understanding the basics of web programming without relying on third-party
libraries.

Objective:
At the end of this exercise, students should be able to:
- Set up a basic web server using the http.server module.
- Handle different types of HTTP requests (GET, POST, etc.).
- Serve JSON data in response to specific endpoints.

Expected Output:
- On visiting http://localhost:8000, you should see the text:
  "Hello, this is a simple API!".
- On accessing the endpoint /data, a JSON response with the sample dataset
  should be returned: {"name": "John", "age": 30, "city": "New York"}.
- When visiting /info, you might see something like:
  {"version": "1.0", "description": "A simple API built with http.server"}.
- Accessing any other undefined endpoint should return a 404 Not Found status
  with a message like "Endpoint not found".
"""

import http.server
import json
import socketserver


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for the simple API server.

    This class handles HTTP requests and routes them to appropriate endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests to different endpoints.

        Endpoints to implement:
        - / : Returns a simple greeting message
        - /data : Returns sample JSON data
        - /info : Returns API information
        - /status : Returns OK status
        - Other paths : Returns 404 Not Found

        TODO: Implement the routing logic for different endpoints
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {"OK"}
            self.wfile.write(json.dumps(status).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error = {"404 Not Found"}
            self.wfile.write(json.dumps(error).encode())

def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving static content on port 8000")
    httpd.serve_forever()


if __name__ == "__main__":
    print("Starting simple HTTP server...")
    print("Server will be available at http://localhost:8000")
    print("Press Ctrl+C to stop the server")
    run()
