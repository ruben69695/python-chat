import time
from server.TCPServer import TCPServer
from server.RequestHandler import RequestHandler

# def client(ip, port, message):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.connect((ip, port))
#         sock.sendall(bytes(message, 'utf8'))
#         response = str(sock.recv(1024), 'utf8')
#         print('Received from server: {}'.format(response))
# client(ip, port, "Hello World, my name is Rubén Arrebola")
# client(ip, port, "This is another message, sended from my machine")
# client(ip, port, "Another interesting message sended from the moon, hey dude I have cookies here!")

if __name__ == "__main__":
    
    HOST = 'localhost'
    PORT = 3000
    server = TCPServer((HOST, PORT), RequestHandler)
    with server:
        server.start()
        while(True):
            # Sleep the thread to avoid hard cpu work
            time.sleep(60)
    server.shutdown()

    