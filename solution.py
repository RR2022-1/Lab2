# import socket module
# Lab 2
from socket import *
# In order to terminate the program
import sys
import fileinput
# port 13331
def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start
    serverSocket.listen(1)
    # Fill in end
    print('web server is up and running on port', port)
    # Fill in line
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # Fill in start      #Fill in end
        try:
            try:
                message = connectionSocket.recv(1024) # get 1024 bytes
                filename = message.split()[1]
                f = open(filename[1:])
                resp1 = 'HTTP/1.0 200 OK\n\n'
                connectionSocket.send(resp1.encode())
                # ------------File Op start--------------------------
                for i in fileinput.input([filename[1:]]):
                    print(i)
                    connectionSocket.send(i.encode())
                # -------------File Op end-----------------------
                connectionSocket.close()
                # Fill in end
            except IOError:
                print("Can't find file")
                # response = 'HTTP/1.0 404 \n\nFile not found'
                # connectionSocket.send(response.encode())
                # connectionSocket.close()
                # pass
                # test -> not found
            # Send response message for file not found (404)
            # Fill in start
                resp2 = 'HTTP/1.0 404\n\nNot Found'
                connectionSocket.send(resp2.encode())
            # Fill in end
            # Close client socket
            # Fill in start
                connectionSocket.close()
            # Fill in end
        except(ConnectionResetError, BrokenPipeError):
           pass
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
