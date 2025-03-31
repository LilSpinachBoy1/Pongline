import socket

# Read the IP to connect to, and store the port
with open("../IP.txt", "r") as f:
    IP = f.readline()
PORT = 65432

# Create a socket to connect to
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))  # Connect to the established server
    s.sendall(b"Adv1n Butt")  # Send some test data
