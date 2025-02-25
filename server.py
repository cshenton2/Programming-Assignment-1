# Christopher Shenton
# Programming Assignment 1
# Purpose: server.py file for listening on a port and receiving client connections.

import socket
import threading

# Define host and port
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

def handle_client(conn, addr):
    """Handles communication with a client."""
    print(f"New connection from {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received from {addr}: {data.decode()}")
        conn.sendall(b"Message received")

    conn.close()
    print(f"Connection with {addr} closed.")

# Main loop to accept multiple clients
while True:
    conn, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
