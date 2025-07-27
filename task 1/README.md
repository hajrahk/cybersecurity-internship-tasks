# Network Sniffer

This project is a simple network packet sniffer written in Python. It captures and displays IP header information from network packets received on a specified network interface.

## Features
- Captures raw IP packets
- Parses and displays IP header fields (version, header length, TTL, protocol, source, and destination IP)
- Runs in promiscuous mode (Windows only)

## Requirements
- Python 3.x
- Windows OS (for promiscuous mode)

## Usage
1. **Edit the script:**
   - Open `sniffer.py` and replace the `HOST` variable with your local IP address.
2. **Run as Administrator:**
   - Open Command Prompt as Administrator (required for raw sockets).
3. **Run the script:**
   ```bash
   python sniffer.py
   ```
4. **Stop the sniffer:**
   - Press `Ctrl+C` to stop capturing packets.

## Notes
- This script requires administrative privileges to run.
- Promiscuous mode is enabled only on Windows.
- For more details, see the `Network Sniffer Report.docx`. 