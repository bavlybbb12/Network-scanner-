# Network Scanner with Dashboard

A Python tool that scans your local network, identifies connected devices, and displays them in a simple live web dashboard — built as hands-on practice alongside networking studies (CS50, Google's *Bits and Bytes of Computer Networking*, and NTI's Cisco Networking Academy courses).

## What It Does

* Sends ARP requests across the local subnet to discover every active device
* Resolves each device's MAC address to a manufacturer name (e.g. "Apple," "TP-Link")
* Displays the results in a clean web dashboard — IP address, MAC address, and vendor for every device currently on the network

This is a live snapshot tool: each time the dashboard is loaded, it runs a fresh scan and shows what is currently connected. It does not store scan history.

## Tech Stack

* **Python 3**
* [**Scapy**](https://scapy.net/) — sends ARP requests and captures replies for device discovery
* [**mac-vendor-lookup**](https://pypi.org/project/mac-vendor-lookup/) — resolves MAC address prefixes to manufacturer names
* **Flask** — serves the web dashboard

## Setup

```bash
# Clone the repository
git clone https://github.com/bavlybbb12/network-scanner.git
cd network-scanner

# Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate   # on Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

**Note:** Scapy requires elevated privileges to send raw ARP packets.

```bash
# Linux / macOS
sudo python3 app.py

# Windows — run your terminal as Administrator, then:
python app.py
```

## Usage

1. Run the app as shown above
2. Open `http://127.0.0.1:5000` in your browser
3. The dashboard will run a live scan of your local subnet and display all connected devices

## Important — Use Responsibly

This tool only scans the local network it is run from. **Only run it on networks you own or have explicit permission to scan** — such as your home Wi-Fi. Scanning networks you do not have permission to scan (university networks, public Wi-Fi, workplace networks without authorization) is not appropriate and may violate network usage policies.

## Roadmap

* \[ ] Store scan history in a database and detect newly connected devices
* \[ ] Add device hostname resolution
* \[ ] Auto-refresh the dashboard on an interval instead of only on page load

## About

Built as part of a self-directed networking and backend engineering learning path, ahead of a networking internship.

**Bavly Toma**
[GitHub](https://github.com/bavlybbb12) · [LinkedIn](https://www.linkedin.com/in/bavly-toma)

