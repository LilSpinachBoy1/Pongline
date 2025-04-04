# https://realpython.com/python-sockets/#echo-client-and-server

import socket

# Set up host IP and port
HOST = "127.0.0.1"
PORT = 65432

# Create function to pass data to the other client
def send_to_oponent(conns: list, sender: int, data: bytes):
    recipient = sender - 1  # Finds the index of the client to send to (clever, ikr)
    rec_conn = conns[recipient]
    rec_conn.sendall(data)

# Set up a socket to use
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # --------- SERVER SETUP ---------
        s.bind((HOST, PORT))  # Bind the socket to the host and port
        s.listen()  # Listen for connections to the server
        print(f"LISTENING FOR CONNECTIONS ON {HOST, PORT}")

        # --------- CONNECTION SETUP ---------
        NUMBER_OF_CONNECTIONS = 2
        connections, addresses = [], []
        for i in range(NUMBER_OF_CONNECTIONS):
            conn, addr = s.accept()  # Store connection details in temp variables
            connections.append(conn)  # Add connection to the connections list
            addresses.append(addr)  # Repeat for the address of the connection
            print(f"Connected to {str(addr)}")  # Output confirmation message

        # --------- GAME SETUP ---------
        ball_pos = [450, 300]
        paddle_positions = [375, 375]

        # --------- GAME LOOP ---------
        game_active = True
        while game_active:
            """
                SEND/RECIEVE LOOP:
                For each client, the following is sent:
                1- The Ball Position
                2- The Opponent Paddle Position
                Then the server listens for:
                1- Player paddle position
                Game data is now up to date!
            """
            # Iterate through connections
            for conn_num, conn in enumerate(connections):
                # Encode ball position
                ball_pos_str = " ".join(list(map(lambda x: str(x), ball_pos)))
                conn.sendall(ball_pos_str.encode("utf-8"))  # Send ball position
                conn.sendall(paddle_positions[conn_num - 1].encode("utf-8"))  # Send position of enemy paddle

                paddle_positions[conn_num] = conn.recv(1024)  # Recieve and update the paddle position

    except KeyboardInterrupt:
        print("Closing server. Goodnight!")

print("End of file")
