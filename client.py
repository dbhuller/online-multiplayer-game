import pygame
from network import Network

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.x -= self.vel
        if keys_pressed[pygame.K_RIGHT]:
            self.x += self.vel
        if keys_pressed[pygame.K_UP]:
            self.y -= self.vel
        if keys_pressed[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

# Read position as string, split and return as int
def read_position(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

# Read tuple value and convert to string
def make_position(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(window, player, player2):
    window.fill((255, 255, 255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()

def main():
    run = True
    # Connecting to server (Network) n
    n = Network()
    start_position = read_position(n.get_position())
    p = Player(start_position[0], start_position[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2_position = read_position(n.send(make_position((p.x, p.y))))
        p2.x = p2_position[0]
        p2.y = p2_position[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(window, p, p2)

main()