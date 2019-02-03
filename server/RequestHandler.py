import threading
import socketserver

class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'utf8')
        cur_thread = threading.current_thread()
        response = bytes("{} : {}".format(cur_thread.name, data), 'utf8')
        self.request.sendall(response)