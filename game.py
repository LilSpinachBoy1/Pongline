import pygame
from pygame.locals import *
import sys
import socket

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
PADDLE_HEIGHT, PADDLE_WIDTH = 150, 25
class Paddle:
    def __init__(self, x_coord: int, colour: tuple = colours["white"]):
        mid = (DISPLAY_SIZE[1] / 2) - (PADDLE_HEIGHT / 2)
        self.rect = pygame.Rect(x_coord, mid, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.colour = colour
        self.SPEED = 4

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[K_w] and self.rect.y > self.SPEED:
            self.rect.move_ip(0, -self.SPEED)
        elif keys[K_s] and self.rect.bottom < DISPLAY_SIZE[1] - self.SPEED:
            self.rect.move_ip(0, self.SPEED)

    def assert_position(self, y_pos: int):
        self.rect.y = y_pos

    def out(self, display):
        pygame.draw.rect(display, self.colour, self.rect)

# Create ball class
class Ball:
    def __init__(self):
        self.SPEED = 2
        self.is_moving = False
        self.centre_coords = [DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 2]
        self.radius = 15
        self.x_direction, self.y_direction = 1, 1

    def toggle_movement(self):
        if not self.is_moving: self.is_moving = True
        elif self.is_moving: self.is_moving = False

    def assert_position(self, pos: tuple[int, int]):
        self.centre_coords = pos
    
    def out(self, display):
        pygame.draw.circle(display, colours["white"], self.centre_coords, self.radius)

# FUNCTION TO RUN GAME
def game():
    # Set up online connection
    IP = "127.0.0.1"
    PORT = 65432

    # Connect to socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))  # Connect to the established server
    data = s.recv(1024).decode("utf-8")
    print(data)

    # Create game objects
    padding = 30
    p_left = Paddle(padding)
    p_right = Paddle(DISPLAY_SIZE[0] - (padding + PADDLE_WIDTH))
    ball = Ball()
    ball.toggle_movement()

    # Create game loop
    running = True
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                s.close()
                pygame.quit()
                sys.exit()

        p_left.movement()

        # Rendering
        DISPLAY.fill(colours["black"])
        ball.out(DISPLAY)
        p_left.out(DISPLAY)
        p_right.out(DISPLAY)
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)  # Tick to new frame after delta time has elapsed
    s.close()

if __name__ == "__main__":
    game()
