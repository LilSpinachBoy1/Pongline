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
# TODO: Change to store coords as array and render at runtime
class Paddle:
    def __init__(self, x_coord: int, colour: tuple = colours["white"]):
        mid = (DISPLAY_SIZE[1] / 2) - (PADDLE_HEIGHT / 2)
        self.x, self.y = x_coord, mid
        self.colour = colour
        self.SPEED = 4

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[K_w] and self.y > self.SPEED:
            self.y -= self.SPEED
        elif keys[K_s] and self.y + PADDLE_HEIGHT < DISPLAY_SIZE[1] - self.SPEED:
            self.y += self.SPEED

    def assert_position(self, y_pos: int):
        self.y = y_pos

    def out(self, display):
        rect = pygame.Rect(self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT)
        pygame.draw.rect(display, self.colour, rect)

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

    def assert_position(self, pos: list[int, int]):
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

    # Create game objects
    padding = 30
    p_left = Paddle(padding)
    p_right = Paddle(DISPLAY_SIZE[0] - (padding + PADDLE_WIDTH))
    ball = Ball()

    # Create game loop
    running = True
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                s.close()
                pygame.quit()
                sys.exit()

        # COMMUNICATIONS
        """
            SEND/RECIEVE LOOP
            First the client listens for:
            1- The ball position
            2- The enemy paddle position
            Then the client sends
            1- Their paddle position
        """
        # 1- Recieve and update ball position
        ball_pos_str = s.recv(1024).decode("utf-8").split()  # Recieves, decodes, and then splits string into a list
        print(f"BALL_POS: Recieved ball coordinates {ball_pos_str} from the server")
        ball_pos = list(map(lambda x: int(x), ball_pos_str))  # Converts the string to an integer array
        ball.assert_position(ball_pos)

        # 2- Recieve and update the paddle position
        enemy_paddle = int(s.recv(1024).decode("utf-8"))
        print(f"OPPONENT_POS: Recieved paddle coordinate {str(enemy_paddle)} from server")
        p_right.assert_position(enemy_paddle)

        # 1- Update and send the paddle position
        p_left.movement()
        s.sendall(str(p_left.y).encode("utf-8"))

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
