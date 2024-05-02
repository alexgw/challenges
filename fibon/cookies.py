from http.server import HTTPServer, BaseHTTPRequestHandler
from http import cookies

PORT = 8080

#current = 1
#prev = 0



class Handler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            C = cookies.SimpleCookie(self.headers.get('Cookie')) 
            print(C.keys()) 
            #setCookies
            if 'prev' not in C.keys() :
                print("setting initial prev")
                C["prev"] = 1
                prev = 1
            else:
                prev = int(C["prev"].value)

            if 'current' not in C.keys():
                print("setting initial current")
                C["current"] = 0
                current = 0
            else:
                current = int(C["current"].value)

            next = prev + current

            
            C["prev"] = current
            C["current"] = next
            C["test"] = "end"

            for morsel in C.values():
                self.send_header("Set-Cookie", morsel.OutputString())
            print(prev, current, C)


            self.end_headers()
            #set the current number to the global number
            #the next number in the sequence is the prev + current
            print(next)
            content = '<html><body style="background: #202020"><p style="color:antiquewhite; margin: auto; padding: 20% 20%; font-size: 20rem; ">' +  str(current) + '</p></body></html>' 
            content = content.encode("UTF8")
            self.wfile.write(content)
            
        



httpd = HTTPServer(('localhost',8080),Handler)
httpd.serve_forever()
