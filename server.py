import socket
from _thread import *
from player import Player
import pickle
from game import Game

server = "192.168.1.5"
port = 5555

# Initialize socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Server listening
s.listen()
print("Waiting for connection on port: " + str(port) + " and server: " + server)

# Dictionary of game objects
games = {}
# stores ip addresses of connected clients
connected = set()
# keeps track of current game id
id_count = 0

def threaded_client(conn, p, game_id):
    global id_count
    conn.send(str.encode(str(p)))
    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            # Check if game still exists
            if game_id in games:
                game = games[game_id]
                if not data:
                    break
                else:
                    # reset game 
                    if data == "reset":
                        game.reset()
                    elif data != "get":
                        game.play(p, data)
                    
                    reply = game
                    conn.sendall(pickle.dump(reply))
            else:
                break
        except:
            break
    print("Lost Connection")
    try:
        del games[game_id]
        print("Closing Game: ", game_id)
    except:
        pass
    id_count -= 1
    conn.close()

# Server always listening for new connections, start new thread, ect
while True:
    # accepts incoming connections from clients and stores (conn obj, IP addr)
    conn, addr = s.accept()
    print("Connected to: ", addr)

    id_count += 1
    p = 0   # current player
    game_id = (id_count - 1) // 2
    # check if num players is odd or even
    # if odd, start new game
    if id_count % 2 == 1:
        games[game_id] = Game(game_id)
        print("Creating a new game...")
    # if even, ready to start game
    else:
        # once two players are connected to game, ready to start game
        games[game_id].ready = True
        p = 1   

    start_new_thread(threaded_client, (conn, p, game_id))
