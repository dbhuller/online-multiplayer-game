import socket
from _thread import *
import sys

server = "192.168.1.5"
port = 5555

# Initialize socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Server listening
s.listen(2)

print("Waiting for connection on port: " + str(port) + " and server: " + server)

def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

# Server always listening for new connections, start new thread, ect
while True:
    # accepts incoming connections from clients and stores (conn obj, IP addr)
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client(), (conn, ))