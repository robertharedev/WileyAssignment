from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>The Best Website</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body><p>Wiley assignment web server!</p></body>", "utf-8"))
        self.wfile.write(bytes("</html>", "utf-8"))

if __name__ == "__main__":        
    PORT = 8000
    webServer = HTTPServer(("0.0.0.0", PORT), MyServer)
    print("Server started http://0.0.0.0:%s" % PORT)
    webServer.serve_forever()
