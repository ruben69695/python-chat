import socketserver
import threading


class TCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
    Provides continue streams of data between client and server using Internet TCP protocol

    ...

    Attributes
    ----------
    ip : str
        An IP address for the server thread
    port : int
        A port to the IP address
    server_thread: threading.Thread
        Creates a server thread using threading.Thread constructor

    Methods
    -------
    start(self)
        Initializes a TCPServer instance server thread
    """

    def __init__(self, server_address, request_handler_class):
        """
        Parameters
        ----------
        server_address : tuple
            A 2 values tuple containing the server IP and port
        request_handler_class : RequestHandler class
            Handles HTTP requests arrived at the server, using the handle() method
        """
        socketserver.TCPServer.__init__(self, server_address, request_handler_class)
        self.ip = server_address[0]
        self.port = server_address[1]
        self.server_thread = threading.Thread(target=self.serve_forever)
        self.server_thread.daemon = True
    
    def start(self):
        """ Starts the instance's server thread 

        Parameters
        ----------
        self : TCPServer Class
            Uses self.ip and self.port attributes to start the server
        
        """
        self.server_thread.start()
        print(f'Server running on {self.ip}:{self.port}')
