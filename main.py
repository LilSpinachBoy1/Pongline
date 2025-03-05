"""
Welcome to main.py!
This is the initial boot file of the program, and will provide a CLI method of setting up a connection.
It should read a file to see if there is a saved IP:
- If there is a saved one, it should prompt the user to either use it again or enter a new one
- If there is not one, it should prompt the user to enter one
Following this, it should boot the game and connect to the server
"""

# Function to take IP as input
def take_IP():
    return input("Please enter the IP address you wish to connect to...\n")

print("Welcome to Ponline!")

# Read the IP file
with open("IP.txt", "r") as f:
    IP = f.readline()

if IP:
    while True:
        use_saved = input("Saved connection IP found, would you like to use it? y/n\n")
        if use_saved.upper() in ["Y", "N"]:  # If valid input
            if use_saved.upper() == "Y":
                print(f"Great! Connecting to {IP}")
            else:
                IP = take_IP()
                print(f"Great! Connecting to {IP}")
            break  # Get out of input check loop
        else:  # Invalid input
            print("Invalid input, please enter y or n...")
else:
    IP = take_IP()

# Write new IP to file
with open("IP.txt", "w") as f:
    f.write(IP)