import pygame
from pawns import *
from board import board
from setup import setup_game

clock = pygame.time.Clock()

# TODO
# Import the board in setup.py and set attributes of pawns classes in setup.py
# Create all classes in board.py
# Fix numbers in StringFEN

def main():
    Run = True

    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    setup_game('rnbqkbnr/pppppppp/////pppppppp/rnbqkbnr')
    while Run == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
            elif event.type == pygame.QUIT:
                Run = False
        clock.tick(60)
        pygame.display.flip()


if __name__ == "__main__":
    main()
