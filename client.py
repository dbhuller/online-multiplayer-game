import pygame
from network import Network
from player import Player

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")



def redrawWindow(window, player, player2):
    window.fill((255, 255, 255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()

def main():
    run = True
    # Connecting to server (Network) n
    n = Network()
    p = n.get_p()

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(window, p, p2)

main()