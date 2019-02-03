import socketserver
import threading

class TCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    
    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)
        self.ip = server_address[0]
        self.port = server_address[1]
        self.server_thread = threading.Thread(target=self.serve_forever)
        self.server_thread.daemon = True
    
    def start(self):
        self.server_thread.start()
        print("Server running on {}:{}".format(self.ip, self.port))
        