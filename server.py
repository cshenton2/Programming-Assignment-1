# Christopher Shenton
# Programming Assignment 1
# Purpose: server.py file for listening on a port and receiving client connections.

import socket

# Define host and port
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Received: {data.decode()}")
    conn.sendall(b"Message received")  # Send response

conn.close()
server_socket.close()
