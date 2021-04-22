import http.server
import urllib.parse as parse
import time

from gpio.config import outputs
from gpio.interface import setup
from gpio.interface import cleanup

hostName = "0.0.0.0"
serverPort = 8081

class MyServer(http.server.SimpleHTTPRequestHandler):    
    def handle_toggle(self, parsed_url):
        query_params = parse.parse_qs(parsed_url.query)
        if ("led" in query_params): 
            color = query_params["led"][0]
            key = color.upper()
            if key in outputs:
                outputs[key].toggle()
                on_or_off = "on" if outputs[key].is_on() else "off"
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(on_or_off, "utf-8")) 

    def handle_state(self, parsed_url):
        query_params = parse.parse_qs(parsed_url.query)
        if ("led" in query_params): 
            color = query_params["led"][0]
            key = color.upper()
            if key in outputs:
                on_or_off = "on" if outputs[key].is_on() else "off"
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(on_or_off, "utf-8")) 
    
    def do_GET(self):
        parsed_url = parse.urlparse(self.path)
        if parsed_url.path == "/toggle":
            self.handle_toggle(parsed_url) 

        elif parsed_url.path == "/state":
            self.handle_state(parsed_url) 

        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":        
    webServer = http.server.HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        setup(outputs)
        webServer.serve_forever()
    except KeyboardInterrupt:
        cleanup()

    webServer.server_close()
    print("Server stopped.")