# Christopher Shenton
# Programming Assignment 1
# Purpose: server.py file for listening on a port and receiving client connections.

import socket
import threading
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# AES 32-byte encryption key
KEY = b'This is a key123This is a key123'

def encrypt(plaintext, key):
    iv = os.urandom(16)  # Generate random IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return iv + ciphertext  # Add IV before encrypted text

def decrypt(ciphertext, key):
    iv = ciphertext[:16]  # Extract IV from ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)
    return plaintext.decode()

def handle_client(conn, addr):
    """Handles communication with a client."""
    print(f"New connection from {addr}")

    while True:
        encrypted_data = conn.recv(1024)
        if not encrypted_data:
            break
        
        # Decrypt received message
        try:
            message = decrypt(encrypted_data, KEY)
            print(f"Received from {addr}: {message}")
        except Exception as e:
            print(f"Decryption error: {e}")
            break

        # Encrypt and send response with key attached
        response = encrypt("Message received", KEY)
        conn.sendall(response)

    conn.close()
    print(f"Connection with {addr} closed.")

# Create and start the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
