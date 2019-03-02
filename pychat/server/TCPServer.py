from pychat.utils.collections import Queue
import selectors
import socket
import time
import types



class TCPServer():
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

    def __init__(self, server_address):
        """
        Parameters
        ----------
        server_address : tuple
            A 2 values tuple containing the server IP and port
        request_handler_class : RequestHandler class
            Handles HTTP requests arrived at the server, using the handle() method
        """
        self.ip = server_address[0]
        self.port = server_address[1]
        self.server_address = server_address
        self.client_sockets_connected = {}
        self.is_socket_opened = True
        self.selector = selectors.DefaultSelector()
    
    def start(self):
        """ Starts the instance's server thread 

        Parameters
        ----------
        self : TCPServer Class
            Uses self.ip and self.port attributes to start the server
        
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.server_address)
        self.socket.listen()
        print(f'Server running on {self.ip}:{self.port}')
        self.socket.setblocking(False)
        self.selector.register(self.socket, selectors.EVENT_READ, data=None)

        while True:
            events = self.selector.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    self.accept_wrapper(key.fileobj)
                else:
                    self.service_connection(key, mask)

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
        print('accepted connection from', addr)
        conn.setblocking(False)      
        self._register_client(addr, conn)

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # Should be ready to read
            if recv_data:
                data.outb += recv_data
            else:
                print('closing connection to', data.addr)
                self.selector.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print('echoing', repr(data.outb), 'to', data.addr)
                sent = sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]

    def _register_client(self, address, sock):
        data = types.SimpleNamespace(addr=address, inb=b'', outb=b'')
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.selector.register(sock, events, data=data)
        self.client_sockets_connected[address] = sock
        print('Client with the address {0} registered'.format(address))


    def shutdown(self):
        self.is_socket_opened = False
        self.socket.close()
        
