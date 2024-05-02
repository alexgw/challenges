from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8080

current = 1
prev = 0

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global current
        global prev
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            #set the current number to the global number
            #the next number in the sequence is the prev + current
            next = prev + current
            content = '<html><body style="background: #202020"><p style="color:antiquewhite; margin: auto; padding: 20% 20%; font-size: 20rem; ">' +  str(next) + '</p></body></html>' 
            content = content.encode("UTF8")
            self.wfile.write(content)
        
            prev = current
            current = next


httpd = HTTPServer(('localhost',8080),Handler)
httpd.serve_forever()
