#!/bin/bash

# Start the server in a new terminal window
echo "Starting server..."
gnome-terminal -- bash -c "python server.py; exec bash"  # Adjust for your terminal

# Wait for server to start
echo "Waiting for server to start..."
sleep 1  # Sleep for 1 second

# Start the client in a new terminal window
echo "Starting client..."
gnome-terminal -- bash -c "python client.py; exec bash"  # Adjust for your terminal
