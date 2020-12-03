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

# COPIED from client.py
# Read position as string, split and return as int
def read_position(str):
    str = str.split(",")
    return int(str[0], int(str[1]))

# Read tuple value and convert to string
def make_position(tup):
    return str(tup[0]) + "," + str(tup[1])
#-------------------------
# List to keep track of position touples of players
position_list = [(0, 0), (100, 100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_position(position_list[player])))
    reply = ""
    while True:
        try:
            # read and update player position
            data = read_position(conn.recv(2048).decode())
            position_list[player] = data
            # reply = data.decode("utf-8")
            

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = position_list[0]
                else:
                    reply = position_list[1]
                print("Recieved: ", data)
                print("Sending: ", reply)

            conn.sendall(str.encode(make_position(reply)))
        except:
            break
    print("Lost Connection")
    conn.close()

current_player = 0
# Server always listening for new connections, start new thread, ect
while True:
    # accepts incoming connections from clients and stores (conn obj, IP addr)
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1