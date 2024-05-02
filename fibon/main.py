from http.server import HTTPServer, BaseHTTPRequestHandler
from http import cookies

PORT = 8080

#current = 1
#prev = 0


def getfib(n):
    current = 0
    prev = 0
    next = 0
    i = 0; 
    while i < n:
        next = prev + current
        #print("current: ", current, "prev: ", prev, "next: ", next)
        #print(next)
        prev = current
        if current == 0:
            next = 1
        current = next
        i += 1
    
    return next



class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            C = cookies.SimpleCookie(self.headers.get('Cookie')) 
            print(C.keys()) 
            #setCookies
            if "count" not in C.keys():
                print("set initial count to 0")
                C["count"] = 0
            else:
                C["count"] = int(C["count"].value) + 1

            for morsel in C.values():
                self.send_header("Set-Cookie", morsel.OutputString())
            
            count = int(C["count"].value)

            self.end_headers()
            #set the current number to the global number
            #the next number in the sequence is the prev + current
            print(count)
            content = '<html><body style="background: #202020"><p style="color:antiquewhite; margin: auto; padding: 20% 20%; font-size: 10vw;; ">' +  str(getfib(count)) + '</p></body></html>' 
            content = content.encode("UTF8")
            self.wfile.write(content)
            
        
        elif self.path[1:].isdigit():
            print("got a number")
            number = int(self.path[1:])
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            #set the current number to the global number
            #the next number in the sequence is the prev + current
            content = '<html><body style="background: #202020"><p style="color:antiquewhite; margin: auto; padding: 20% 20%; font-size: 10vw;; ">' +  str(getfib(number)) + '</p></body></html>' 
            content = content.encode("UTF8")
            self.wfile.write(content)


httpd = HTTPServer(('localhost',8080),Handler)
httpd.serve_forever()
