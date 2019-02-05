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

def print_instructions():
    print("Instructions:\n-> python main.py -h [HOST] -p [PORT]")

def get_args(args, default_host, default_port, bad_args = False):
    result = [bad_args, default_host, default_port]
    saved_parameter = ''

    if len(args) > 1:
        for index, cur_parameter in enumerate(args):         
            if saved_parameter == '-h':
                result[1] = cur_parameter
            elif saved_parameter == '-p':
                result[2] = int(cur_parameter)            

            if cur_parameter == '-h':
                saved_parameter = cur_parameter
            elif cur_parameter == '-p':
                saved_parameter = cur_parameter
            else:
                saved_parameter = ''

            if saved_parameter != '' and index + 1 >= len(args):
                result[0] = True
                print("Bad arguments...\n")
                print_instructions()
                break

    return result


if __name__ == "__main__":
    
    HOST = 'localhost'
    PORT = 3000
    EXIT = False

    # Get arguments passed on the command-line and assigns them to Host, Port and exit
    EXIT, HOST, PORT = get_args(sys.argv, default_host=HOST, default_port=PORT, bad_args=EXIT)

    # If there is not a bad argument, initialize the server
    if EXIT == False:
        server = TCPServer((HOST, PORT), RequestHandler)
        with server:
            server.start()
            while(True):
                # Sleep the thread to avoid hard cpu work
                time.sleep(60)
        server.shutdown()