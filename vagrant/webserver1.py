from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
class webserver(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello1"):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output=""
                output+="<html><body>Second hello</body></html>"
                self.wfile.write(output)
                print output
                return


        except IOError:
            self.send_error(404,"File not found%s"%self.path)
            
            




def main():
    try:
        port=8080
        server=HTTPServer(('',port),webserver)
        print "Webserver Running at 8080"
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C Pressed"
        server.socket.close()
        




if __name__=='__main__':
    main()
