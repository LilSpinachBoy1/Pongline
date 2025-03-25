import socket

# Set up host IP and port
HOST = "127.0.0.1"
PORT = 65432

# Set up a socket to use
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST, PORT))  # Bind the socket to the host and port
        s.listen()  # Listen for connections to the server
        print(f"LISTENING FOR CONNECTIONS ON {HOST, PORT}")

        # -------- FIRST CONNECTION --------
        conn1, addr1 = s.accept()  # Accept first connection
        print(f"Connected to {str(addr1)}")
        test_data = conn1.recv(1024)
        if test_data.decode("utf-8") == "Adv1n Butt":
            print("Test data successfully recieved from connection 1!")
        else:
            raise InterruptedError

        # -------- SECOND CONNECTION --------
        conn2, addr2 = s.accept()
        print(f"Connected to {str(addr2)}")
        test_data = conn2.recv(1024)
        if test_data.decode("utf-8") == "Adv1n Butt":
            print("Test data successfully recieved from connection 2!")
        else:
            raise InterruptedError


    except KeyboardInterrupt:
        print("Closing server. Goodnight!")
    except InterruptedError:
        print("Issue connecting to client, goodnight...")
