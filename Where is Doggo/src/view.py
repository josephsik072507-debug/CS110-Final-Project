import pygame
from pygame import Surface

class GameView:
    """
    Responsible only for drawing. No logic.
    """

    def __init__(self, model):
        self.model = model
        self.font_large = pygame.font.SysFont(None, 48)
        self.font_small = pygame.font.SysFont(None, 25)

        self.screen = pygame.display.set_mode(model.SCREEN_SIZE)
        pygame.display.set_caption("Where Is Doggo?")
        pygame.display.set_icon(model.big_dog)

    def draw_background(self):
        self.screen.blit(self.model.background, (0, 0))

    def draw_small_dog(self):
        self.screen.blit(self.model.small_dog, self.model.small_dog_rect.topleft)
        pygame.draw.rect(self.screen, (255, 255, 255), self.model.small_dog_rect, 2)

    def draw_big_example(self):
        self.screen.blit(self.model.big_dog, (100, 100))
        self.draw_text("This is a dog, find it here", 200, 90, (0, 255, 0))

    def draw_found_count(self):
        text = self.font_small.render(
            f"Doggos Found: {self.model.found_count}", True, (255, 255, 255)
        )
        self.screen.blit(text, (450, 0))

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        surf = self.font_large.render(text, True, color)
        rect = surf.get_rect(center=(x, y))
        self.screen.blit(surf, rect)

    def render(self):
        """Draw the entire frame."""
        self.draw_background()
        self.draw_small_dog()
        self.draw_found_count()

        if self.model.found_count >= 10:
            self.draw_text("You found all the Doggos!", 
                           self.model.SCREEN_WIDTH // 2, 50, (0, 255, 0))
        else:
            self.draw_big_example()

        pygame.display.flip()