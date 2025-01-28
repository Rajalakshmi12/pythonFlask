# api/index.property
import json
from http.server import BaseHTTPRequestHandler

class handler():
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message":"Hello!"}).encode('utf-8'))
        return
        