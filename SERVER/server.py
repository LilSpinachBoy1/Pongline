# https://realpython.com/python-sockets/#echo-client-and-server

import socket

# Set up host IP and port
HOST = "0.0.0.0"
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
            send_to_oponent(connections, 1, b"Hello first client!")

        send_to_oponent(connections, 0, b"Hello second client!")

    except KeyboardInterrupt:
        print("Closing server. Goodnight!")

print("End of file")
