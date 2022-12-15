

from http.server import HTTPServer,BaseHTTPRequestHandler

content ="""
<html>
<body>
<title>Django</title>
</head>
<body>
<h1>Django</h1>
<p>This is Web Application Framework written in python</p>

</body>
</html>
"""

class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
    
server_address=('',8001)
httpd=HTTPServer(server_address,WebHandler)
print("Web server running...")
httpd.serve_forever()         
