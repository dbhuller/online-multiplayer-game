import socket
from _thread import *
from player import Player
import pickle

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


players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            # read and update player position
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            # reply = data.decode("utf-8")
            

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Recieved: ", data)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
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