# Task 1: Consume data from an API using command line tools (curl)

## Installation and Basic Usage

### Check curl installation:
```bash
curl --version
```

### Basic webpage fetch:
```bash
curl http://example.com
```

## API Interaction Examples

### Fetch posts from JSONPlaceholder:
```bash
curl https://jsonplaceholder.typicode.com/posts
```

### Fetch only headers:
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

### Make a POST request:
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### POST with JSON data:
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"foo","body":"bar","userId":1}' \
  https://jsonplaceholder.typicode.com/posts
```

## Useful curl Options

| Option | Description | Example |
|--------|-------------|---------|
| `-I` | Fetch headers only | `curl -I example.com` |
| `-X` | Specify HTTP method | `curl -X POST example.com` |
| `-d` | Send data | `curl -d "key=value" example.com` |
| `-H` | Add header | `curl -H "Content-Type: application/json"` |
| `-v` | Verbose output | `curl -v example.com` |
| `-o` | Save output to file | `curl -o output.json example.com` |

## Expected Outputs

### Version check:
```
curl 7.68.0 (x86_64-pc-linux-gnu) libcurl/7.68.0
Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
Features: AsynchDNS brotli GSS-API HTTP2 HTTPS-proxy IDN IPv6 Kerberos LDAP libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP UnixSockets
```

### Headers only:
```
HTTP/2 200
content-type: application/json; charset=utf-8
content-length: 27986
```

### POST response:
```json
{
  "title": "foo",
  "body": "bar", 
  "userId": 1,
  "id": 101
}
```