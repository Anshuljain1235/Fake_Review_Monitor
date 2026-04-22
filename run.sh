#!/bin/bash

echo "========================================"
echo "  Fake Review Monitor - Starting..."
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "[1/3] Checking dependencies..."
if ! python3 -c "import flask" &> /dev/null; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
else
    echo "Dependencies already installed"
fi

echo ""
echo "[2/3] Starting Flask server..."
echo ""
echo "========================================"
echo "  Server will start at:"
echo "  http://127.0.0.1:5000"
echo "========================================"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the Flask app
python3 app.py
