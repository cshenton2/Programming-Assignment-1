# Design Explanation Document

This document outlines the design of a client-server application implemented in Python. It describes the communication mechanism between the client and server, the threading model used for handling multiple clients, and the encryption approach employed to secure data transmission.

## Client-Server Communication

### Overview
The application uses a TCP-based socket connection to facilitate communication between a single server and one or more clients. The server listens for incoming connections on a predefined host (`127.0.0.1`) and port (`12345`), while the client initiates a connection to this address.

### Communication Flow
1. **Connection Establishment**:
   - The server creates a TCP socket using `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`, binds it to `HOST:PORT`, and listens for incoming connections with `server_socket.listen()`.
   - The client creates a similar TCP socket and connects to the server using `client_socket.connect((HOST, PORT))`.

2. **Data Exchange**:
   - **Client to Server**: The client sends a series of plaintext messages (e.g., "Hello World!", "Testing Testing", "Goodbye!") to the server. Each message is encrypted before transmission (see Encryption Implementation below) and sent via `client_socket.sendall()`.
   - **Server to Client**: Upon receiving an encrypted message, the server decrypts it, processes it (logging the plaintext), and responds with an encrypted "Message received" string sent via `conn.sendall()`.

3. **Termination**:
   - The client sends a predefined list of messages and closes the connection with `client_socket.close()` after receiving responses.
   - The server closes the connection with a specific client when no more data is received (`conn.recv(1024)` returns empty), but it continues listening for new connections in an infinite loop.

### Protocol Details
- **Transport Layer**: TCP ensures reliable, ordered delivery of messages.
- **Message Format**: Messages are encrypted byte strings prefixed with a 16-byte initialization vector (IV) for AES encryption. No explicit message framing is used; the application relies on TCP’s stream handling and fixed buffer size (`1024` bytes).

## Chosen Threading Model

### Threading Model
The server employs a **multi-threaded** design to handle multiple clients concurrently.

- **Implementation**:
  - The main server loop runs in the primary thread, continuously accepting new client connections with `server_socket.accept()`.
  - For each new connection, a dedicated thread is spawned using `threading.Thread(target=handle_client, args=(conn, addr))`. The `handle_client` function manages all communication with that client.
  - Each client thread runs independently, receiving, decrypting, and responding to messages until the client disconnects.

- **Why Threading?**:
  - **Simplicity**: Threading is straightforward for a small-scale server where each client’s communication is independent and blocking I/O operations (like `conn.recv()`) are used.
  - **Concurrency**: Allows the server to handle multiple clients simultaneously without blocking the main loop, which continues accepting new connections.
  - **Suitability**: Fits the assignment’s likely scope, avoiding the complexity of asynchronous programming (e.g., `asyncio`) for basic client-server interaction.

- **Trade-offs**:
  - **Resource Usage**: Each thread consumes system resources, which could become inefficient with many clients (e.g., hundreds). However, for a small number of clients, this is negligible.
  - **No Async Alternative**: Asynchronous I/O wasn’t chosen due to the simplicity of the task and the blocking nature of the current socket operations.

## Encryption Implementation

### Overview
Data security is ensured using the **AES (Advanced Encryption Standard)** symmetric encryption algorithm in **CBC (Cipher Block Chaining)** mode, provided by the `Crypto.Cipher` module from the `pycryptodome` library.

### Key Components
1. **Encryption Key**:
   - A static 32-byte key is defined as `KEY = b'This is a key123This is a key123'`.
   - This key is hardcoded and shared between client and server, simulating a pre-shared key scenario. In a real-world application, key exchange (e.g., Diffie-Hellman) would be used.

2. **Initialization Vector (IV)**:
   - A 16-byte random IV is generated for each message using `os.urandom(16)`.
   - The IV is prepended to the ciphertext and sent with the message, ensuring it’s available for decryption without separate transmission.

3. **Padding**:
   - Messages are padded to match AES’s 16-byte block size using `pad()` and `unpad()` from `Crypto.Util.Padding`. This ensures compatibility with block-based encryption.

### Encryption/Decryption Process
- **Encryption** (`encrypt` function):
  1. The plaintext is encoded to bytes (`.encode()`).
  2. Padding is applied to align with the block size.
  3. A new AES cipher object is created with the key, CBC mode, and random IV.
  4. The padded plaintext is encrypted, and the IV is concatenated with the ciphertext.
- **Decryption** (`decrypt` function):
  1. The IV is extracted from the first 16 bytes of the received data.
  2. A new AES cipher object is created with the key, CBC mode, and extracted IV.
  3. The remaining ciphertext is decrypted and unpadded to retrieve the original plaintext.

### Security Considerations
- **Strengths**:
  - AES-CBC with a random IV per message provides confidentiality and prevents pattern analysis across identical plaintexts.
  - The 256-bit key length (32 bytes) is robust against brute-force attacks.
- **Weaknesses**:
  - The hardcoded key eliminates key distribution security, making it vulnerable if the code is exposed.
  - No integrity check (e.g., HMAC) means tampered messages could be processed without detection.
  - Error handling is minimal; decryption failures (e.g., wrong key or corrupted data) are logged but don’t gracefully recover.

## Conclusion
This design provides a functional client-server system with encrypted communication and multi-client support via threading. It prioritizes simplicity and reliability for an educational context, while demonstrating core concepts like socket programming, concurrency, and symmetric encryption. Future improvements could include dynamic key exchange, message integrity checks, and an asynchronous model for scalability.