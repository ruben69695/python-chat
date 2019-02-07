import threading
import socketserver

class RequestHandler(socketserver.BaseRequestHandler):
    """
    Handles HTTP request made to the server, being instantiated
    with each request. Extends BaseRequestHandler.

    ...

    Methods
    -------
    handle(self):
        Process incoming requests
    """

    def handle(self):
        """ Method that handles each request made to the server

        Raises
        ------
        None
        """

        data = str(self.request.recv(1024), 'utf8')
        cur_thread = threading.current_thread()
        response = bytes("{} : {}".format(cur_thread.name, data), 'utf8')
        self.request.sendall(response)