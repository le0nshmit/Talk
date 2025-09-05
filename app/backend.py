import socket
import threading
import sys

# class for backend functions
class Backend:
    def __init__(self):
        self.HOST = '127.0.0.1'             # host ip is local
        self.PORT = 55555                   # host port
        self.SERVER = None                  # creates server obj
        self.clients = []                   # creates list for clients

    # function to setup server
    def setup(self):
        self.SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # create server that uses ipv4 and tcp
        self.SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # allow server to connect to port in 'time wait' state
        self.SERVER.bind((self.HOST, self.PORT))                            # set servers ip and port
        self.SERVER.listen()                                                # tells server to listen for connections

        print('[SERVER] listening')

        accept_thread = threading.Thread(target=self.accept_connections, daemon=True)   # creates a daemon thread to run accept connections 
        accept_thread.start()                                                           # starts thread

    def accept_connections(self):
        while True:
            conn, addr = self.SERVER.accept()                               # gets connection and address from client

            handle_thread = threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True)     # creates a daemon thread to run client handling
            handle_thread.start()                                                                           # starts thread

            
    def handle_client(self, conn, addr):
        print(f"{addr} Joined!")                                                                            # prints user joined
        self.clients.append(conn)                                                                           # appends user connection to client list

        try:                                                                                                    
            while True:                                                                                     # loop to buffer data
                data = conn.recv(16)                                                                      # receive data
                if not data:                                                                                
                    break                                           
                print(f"[SERVER] {data}")                                                           

                for client in self.clients:
                    if client != conn:
                        client.sendall(f"[SERVER] {data.encode()}")
        except ConnectionResetError:
            pass
        finally:
            try:
                self.clients.remove(conn)
            except ValueError:
                pass
        conn.close()
            

    # main function for host
    def Host(self):
        self.setup()                                                        # calls setup function
        while True:         
            cmd = input("Cmd> ")                                            # allows server side to input commands
            if cmd == "quit":                                               # if command quit then break
                break
            else:
                print("Unknown Command")



    


if __name__ == "__main__":
    backend = Backend()
    if sys.argv[1] == "host":
        backend.Host()
    else:
        print("Unknown")