import pygame
import sys
from menu import run_menu
from game import run_game
#main loop of the game. 
def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Angry Birds 2P")
    clock = pygame.time.Clock()

    while True:
        players = run_menu(screen, clock)
        if players == "quit":
            break

        result = run_game(screen, clock, players)
        if result == "quit":
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
