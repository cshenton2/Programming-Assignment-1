PYTHON := python3
# Command to build files (not needed for Python)
build:
	@echo "Nothing to build."
# Command to run the server and client together
run:
	@echo "Starting server..."
	@$(PYTHON) server.py &
	@sleep 1  # Wait for server to start
	@echo "Starting client..."
	@$(PYTHON) client.py

# Commands to run either server or client respectively
run-server:
	@echo "Starting server..."
	@$(PYTHON) server.py &

run-client:
	@echo "Starting client..."
	@$(PYTHON) client.py
# Command to clean any potential excess files created by Python
clean:
	@echo "Cleaning up excess files"
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} +