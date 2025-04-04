# Communications outline

---
## The role of client and server
### Client
The client's role is to render an output to the user, and to take input of their movement.
### Server
The server should set up connections between the players, and process the ball movement. It should detect when points are scored, and should prompt when a user has enough points to win.

---
## A typical game:
1. Server sets up socket and establishes connection with both clients
2. Server begins broadcasting ball locations, and clients output them to the screen
3. Clients send paddle location to server, which passes it to the other client to be rendered
4. Client checks for paddle collisions, and reports them to the server
5. Server resets ball when points are scored
6. Server sends win message when game is won, and disconnects

---
## Message types

- PADDLE_POS: A single y coordinate for the paddle
- BALL_POS: A tuple containing the coordinates of the ball
- PADDLE_COLLISION: A boolean flag checking if there is a collision with a paddle
- OPPONENT_POS: A single y coordinate of where the oponent paddle should be
- VICTORY: Indicates a player has won
- LOSS: Indicates a player has lost