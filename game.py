import pygame
import sys

# Create Colour Pallette
colours = {
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}

# Initialise window
DISPLAY_SIZE = (900, 600)
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("Pongline")
FPS = 60

# Create Paddle Class
class Paddle:
    def __init__(self, x_coord: int, colour: tuple = colours["white"]):
        self.rect = pygame.Rect()

# Create game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Rendering
    DISPLAY.fill(colours["black"])
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)  # Tick to new frame after delta time has elapsed