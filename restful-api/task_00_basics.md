# Task 0: Basics of HTTP/HTTPS

## Summary of HTTP vs HTTPS

### Key Differences:
- **HTTP (HyperText Transfer Protocol)**: Unencrypted communication protocol
- **HTTPS (HTTP Secure)**: HTTP with SSL/TLS encryption layer

### Security Aspects:
- HTTP: Data transmitted in plain text, vulnerable to eavesdropping
- HTTPS: Data encrypted during transmission, protects against man-in-the-middle attacks

## HTTP Request/Response Structure

### HTTP Request Structure:
```
GET /path HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

### HTTP Response Structure:
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

## Common HTTP Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| GET | Retrieves data | Fetching a web page or API data |
| POST | Creates new resource | Submitting form data, creating user |
| PUT | Updates entire resource | Replacing user profile |
| PATCH | Partial update | Updating specific fields |
| DELETE | Removes resource | Deleting user account |

## Common HTTP Status Codes

| Code | Description | Scenario |
|------|-------------|----------|
| 200 | OK | Successful request |
| 201 | Created | Resource successfully created |
| 400 | Bad Request | Invalid request format |
| 401 | Unauthorized | Authentication required |
| 404 | Not Found | Requested resource doesn't exist |
| 500 | Internal Server Error | Server-side error occurred |

## Status Code Categories:
- **1xx**: Informational responses
- **2xx**: Successful responses  
- **3xx**: Redirection messages
- **4xx**: Client error responses
- **5xx**: Server error responses