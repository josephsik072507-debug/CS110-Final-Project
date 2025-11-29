import pygame
import random

class DoggoModel:
    """
    Stores all game data and logic.
    """

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 750
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    def __init__(self):
        # Load assets
        self.big_dog = pygame.image.load(
            r"C:\Users\josep\Downloads\Where is Doggo\Assets\annoyingdog.png"
        )
        self.small_dog = pygame.image.load(
            r"C:\Users\josep\Downloads\Where is Doggo\Assets\annoyingdog_smallest.png"
        )
        self.background = pygame.image.load(
            r"C:\Users\josep\Downloads\Where is Doggo\Assets\pygamebg3.png"
        )

        pygame.mixer.music.load(
            r"C:\Users\josep\Downloads\Where is Doggo\Assets\I Really Want to Stay At Your House [8 Bit Tribute to Hallie Coggins and Rosa Walton] 8 Bit Universe.mp3"
        )
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        # Dog positions
        self.positions = [
            (110, 675),
            (765, 215),
            (295, 400),
            (10, 10),
            (990, 10),
            (10, 740),
            (990, 740)
        ]

        # State
        self.found_count = 0
        self.small_dog_rect = None
        self.place_new_small_dog()

    def place_new_small_dog(self):
        """Moves the small dog to a new random location."""
        pos = random.choice(self.positions)
        self.small_dog_rect = self.small_dog.get_rect(topleft=pos)

    def check_click(self, pos):
        """
        Called by controller when mouse is clicked.
        Returns True if small dog was found.
        """
        if self.small_dog_rect.collidepoint(pos):
            self.found_count += 1
            self.place_new_small_dog()
            return True
        return False
