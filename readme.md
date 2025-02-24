# Assignment 1: Simple Client-Server Communication

## Introduction
This project involves implementing a basic client-server model using TCP sockets to facilitate communication between a server and multiple clients. The server will listen for incoming connections, process messages sent by clients, log these messages, and send an acknowledgment back. The client will establish a connection, send a user-provided message, and display the server's response.

The goal of this assignment is to introduce socket programming, multi-threaded or asynchronous network handling, and encryption basics in network communication. This project will provide hands-on experience with TCP/IP protocols, secure messaging, and best practices in software development.

## Project Requirements

### GitHub Repository
- Store the project in a private GitHub repository.
- Maintain a proper commit history showing progressive development.

### TCP Server Implementation
- Listens on a specific port.
- Accepts multiple client connections.
- Receives and logs messages from clients.
- Sends acknowledgment responses to clients.
- Uses basic encryption for message transmission (e.g., OpenSSL, PyCrypto, or equivalent).

### TCP Client Implementation
- Connects to the server.
- Sends a user-provided message.
- Receives and displays the acknowledgment from the server.
- Implements basic encryption for secure message transmission.

### Error Handling
- Implement error detection and handling for failed connections.
- Ensure the server gracefully manages multiple clients and unexpected disconnections.

### Multi-Threading/Async Handling
- The server must support multiple clients using either multi-threading or an asynchronous approach.

## Project Structure and Submission

### Makefile Commands
- **make build** - Compile the project (if applicable).
- **make run** - Start the server and client.
- **make clean** - Remove compiled files.

### Installation & Setup
1. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Start the server:
   ```sh
   make run
   ```
3. Run the client:
   ```sh
   python client.py
   ```

### Dependencies
- Python 3.x
- Required libraries (e.g., `socket`, `threading`, `cryptography`, `OpenSSL`)

### Design Explanation Document
- Describes client-server communication.
- Explains chosen threading/async model.
- Provides an overview of encryption implementation.