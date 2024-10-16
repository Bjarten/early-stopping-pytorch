#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Create a virtual environment if it doesn't already exist
if [ ! -d "venv" ]; then
  echo "Creating a virtual environment in venv..."
  python3 -m venv venv
  echo "Virtual environment created."
else
  echo "Virtual environment already exists."
fi

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip and install dependencies
echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing development dependencies..."
pip install -r requirements-dev.txt

echo "Installing runtime dependencies..."
pip install -r requirements.txt

echo "Development environment is set up and ready to go!"

# To active the virtual environment, run the following command
echo "source venv/bin/activate"