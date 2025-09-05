import socket
import threading

# class for backend functions
class Backend:
    def __init__(self):
        self.HOST = '127.0.0.1'             # host ip is local
        self.PORT = 55555                   # host port
        self.SERVER = None                  # creates server obj
        self.clients = []                   # creates list for clients

    # function to setup server
    def setup(self):
        self.SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # set server to use ipv4 and tcp
        self.SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # allow server to connect to port in 'time wait' state
        self.SERVER.bind((self.HOST, self.PORT))                            # set servers ip and port
        self.SERVER.listen()                                                # tells server to listen for connections

        print('[SERVER] listening')

    # main function for host
    def Host(self):
        self.setup()                                                        # calls setup function
        while True:         
            cmd = input("Cmd> ")                                            # allows server side to input commands
            if cmd == "quit":                                               # if command quit then break
                break
            else:
                print("Unknown Command")