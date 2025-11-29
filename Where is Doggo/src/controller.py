import pygame
from src.model import DoggoModel
from src.view import GameView

class GameController:
    """
    Handles all events, passes them to model,
    and asks view to redraw.
    """

    def __init__(self):
        self.model = DoggoModel()
        self.view = GameView(self.model)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.view.render()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        """Handles all pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.model.check_click(pos)

    def update(self):
        """Game logic would go here if needed."""
        pass