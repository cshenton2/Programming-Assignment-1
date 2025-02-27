PYTHON := python
# Command to build files (not needed for Python)
build:
	@echo "Nothing to build."

# Command to run the server and client together (used a .bat )
run:
	@run.bat

# Commands to run either server or client respectively
run-server:
	@echo "Starting server..."
	@$(PYTHON) server.py

run-client:
	@echo "Starting client..."
	@$(PYTHON) client.py

# Command to clean any potential excess files created by Python
clean:
	@echo "No files to clean up."