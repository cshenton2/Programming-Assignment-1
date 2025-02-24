# Christopher Shenton
# Programming Assignment 1
# Purpose: client.py file for connecting to the server and receiving an acknowledgement.

import socket

# Define host and port
HOST = '127.0.0.1'  # Server's IP
PORT = 65432        # Port to connect to

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Send message
message = "Hello, Server!"
client_socket.sendall(message.encode())

# Receive response
data = client_socket.recv(1024)
print(f"Server says: {data.decode()}")

client_socket.close()
