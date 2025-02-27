# Select interpreter (python3 by default)
PYTHON := python3

ifeq ($(OS),Windows_NT)  # Check if user is on Windows
	PYTHON := python
	SCRIPT := run.bat
else  # Linux/macOS
	SCRIPT := run.sh
endif

# Command to build files (not needed)
build:
	@echo "Nothing to build."

# Command to run the server and client together (using the OS-specific script)
run:
	@echo "Running server and client..."
	@$(SCRIPT)  # Run the appropriate script for the OS

# Commands to run either server or client respectively
run-server:
	@echo "Starting server..."
	@$(PYTHON) server.py

run-client:
	@echo "Starting client..."
	@$(PYTHON) client.py

# Command to clean any potential excess files (not needed)
clean:
	@echo "No files to clean up."
