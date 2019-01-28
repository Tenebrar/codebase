from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8080

with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# Or use:
# python -m http.server 8080
# in a folder with an index.html

# TODO Can I pass a url to my computer to hacker.org? Try at home
