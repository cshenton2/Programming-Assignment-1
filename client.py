# Christopher Shenton
# Programming Assignment 1
# Purpose: client.py file for connecting to the server and receiving an acknowledgement.

import socket
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
    iv = ciphertext[:16]  # Extract IV from cyphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)
    return plaintext.decode()

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Collect messages from user
messages = []
print("Enter your messages (type 'send' on a new line when finished):")
while True:
    message = input("> ")
    if message.lower() == 'send':
        break
    messages.append(message)

# Send all collected messages (encrypted)
for message in messages:
    encrypted_message = encrypt(message, KEY)
    client_socket.sendall(encrypted_message)

    # Receive encrypted response
    encrypted_response = client_socket.recv(1024)
    
    # Decrypt response
    decrypted_response = decrypt(encrypted_response, KEY)
    print(f"Server: {decrypted_response}")

client_socket.close()