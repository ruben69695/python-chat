import time
import sys
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
    
    params = sys.argv
    HOST = 'localhost'
    PORT = 3000
    EXIT = False

    saved_parameter = ''
    for index, cur_parameter in enumerate(params):
        
        if saved_parameter == '-h':
            HOST = cur_parameter
        elif saved_parameter == '-p':
            PORT = int(cur_parameter)            

        if cur_parameter == '-h':
            saved_parameter = cur_parameter
        elif cur_parameter == '-p':
            saved_parameter = cur_parameter
        else:
            saved_parameter = ''

        if saved_parameter != '' and index + 1 >= len(params):
            EXIT = True
            print("Bad arguments...\n")
            print("Intructions:\n-> python main.py -h [HOST] -p [PORT]")
            break;
            

    if EXIT == False:
        server = TCPServer((HOST, PORT), RequestHandler)
        with server:
            server.start()
            while(True):
                # Sleep the thread to avoid hard cpu work
                time.sleep(60)
        server.shutdown()