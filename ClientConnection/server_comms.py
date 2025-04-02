import socket

IP = "127.0.0.1"
PORT = 65432

# Create a socket to connect to
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))  # Connect to the established server
    data = s.recv(1024).decode("utf-8")
    print(data)

print("End of file")
