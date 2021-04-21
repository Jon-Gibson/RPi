import http.server
import urllib.parse as parse
import time

hostName = "localhost"
serverPort = 9191

class MyServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = parse.urlparse(self.path)
        if parsed_url.path == "/toggle":
            query_params = parse.parse_qs(parsed_url.query)
            if ("led" in query_params):
                color = query_params["led"][0]
                print(color)
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":        
    webServer = http.server.HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")