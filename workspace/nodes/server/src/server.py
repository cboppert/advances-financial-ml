from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class AIServer(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.end_headers()
    self.wfile.write(bytes("<html><head><title>Project Server</title></head>", "utf-8"))
    self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8")) # Syntax check here, is this how interpolation works?
    self.wfile.write(bytes("<body>", "utf-8"))
    self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
    self.wfile.write(bytes("</body></html>", "utf-8"))

  if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), AIServer) # Syntax check here, does that create a tuple for the first argument?
    print("Server started http://%s:%s" % (hostName, serverPort)) # Interpolation it must be, but maybe this is just a list in general, bet I can get a third arg there... weird wouldn't just use square brackets... is that not an array syntax in Python? The mystery abounds

    try:
      webServer.serve_forever()
    except KeyboardInterrupt:
      pass

    webServer.server_close()
    print("Server stopped.")
