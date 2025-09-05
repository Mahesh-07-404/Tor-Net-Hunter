#!/bin/bash
set -e

echo "======================================"
echo "     TorNetHunter Installer (Linux)   "
echo "======================================"

# Update packages
echo "[*] Updating system..."
sudo apt update -y

# Install required system packages
echo "[*] Installing system packages: python3 python3-pip tor curl"
sudo apt install -y python3 python3-pip tor curl

# Ensure pip is available
if ! command -v pip3 > /dev/null 2>&1; then
  echo "[!] pip3 not found; aborting."
  exit 1
fi

echo "[*] Installing Python dependencies..."
pip3 install --user -r requirements.txt --break-system-packages

# Make tornethunter executable
echo "[*] Setting executable permissions..."
chmod +x tornethunter.py

# Create log dir
mkdir -p ~/TorNetHunter/logs

# Create global command (user-level)
BIN_PATH="$HOME/.local/bin"
mkdir -p "$BIN_PATH"
cp tornethunter.py "$BIN_PATH/tornethunter"
chmod +x "$BIN_PATH/tornethunter"

echo "======================================"
echo " Installation Completed Successfully! "
echo " Add $BIN_PATH to your PATH if not already."
echo " You can run TorNetHunter using: tornethunter"
echo "======================================"
