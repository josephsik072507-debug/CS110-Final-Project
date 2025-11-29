import pygame
from src.controller import GameController

def main():
    pygame.init()
    pygame.mixer.init()

    controller = GameController()
    controller.run()

if __name__ == "__main__":
    main()
