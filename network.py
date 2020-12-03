import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.5"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.position = self.connect()
        # print(self.id)

    def get_position(self):
        return self.position

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
            
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

# For Testing:
# n = Network()
# print(n.send("Hello"))
# print(n.send("Im working"))