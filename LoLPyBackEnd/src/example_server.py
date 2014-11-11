'''LoLPyBackEnd
Test HTTP Server
To be run locally
http://127.0.0.1:8080/
'''

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
#from ..LoLStatsAnal import riotapi_py

#from os import curdir, sep

#PORT_NUMBER = 8080

class MyHandler(BaseHTTPRequestHandler):
    '''Server handler class.'''

    def do_GET(self):
        '''Handler for GET requests.'''
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hello World!")
        return

#try:
#    server = HTTPServer(('', PORT_NUMBER), MyHandler)
#    print "Started HTTPServer on port ", PORT_NUMBER
#    server.serve_forever()
#except KeyboardInterrupt:
#    print "Port closed."
#    server.socket.close()


