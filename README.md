Local Network & Port Scanner Dashboard
A modular, browser-based network discovery tool built with Python, Scapy, and Flask. This application automatically detects your local subnet (even while completely offline), scans the network for active hosts using Layer 2 ARP broadcasts, looks up hardware MAC vendors, probes common communication ports at Layer 4, and visualizes everything in a clean web dashboard.

Features
Dynamic Subnet Auto-Detection: Automatically discovers your local network card's configuration and fills in the target range (e.g., 192.168.1.0/24) even if you are offline.

Layer 2 Discovery: Uses Scapy to send raw ARP requests for rapid, highly accurate host detection.

Layer 4 Port Scanning: Probes active devices for open common services (HTTP, HTTPS, SSH, SMB, etc.) with strict connection timeouts to prevent script hanging.

Cross-Platform Privilege Guard: Detects user permissions natively on Windows or Linux/macOS before launching, warning the user if administrative/root rights are missing.

Modular Codebase: Implements a strict separation of concerns across core scanner, general utilities, and web server modules.

Data Persistence: Automatically dumps successful scan outputs into a clean JSON log file (network_devices.json).

File Architecture
Plaintext
/Project_Folder
│
├── scanner.py          # The core engine: Crafts packets and probes TCP ports
├── utils.py            # The utility toolbox: Handshakes, OS privilege checks, JSON exports
├── app.py              # The traffic cop: Coordinates backend functions with web routes
│
└── templates/          
    └── index.html      # The frontend UI: Built with Jinja2 loops and Bootstrap 5
Requirements & Installation
1. System Dependency (Packet Sniffing)
Because this application crafts raw network packets, your operating system needs a packet-capture driver:

Windows: Download and install Npcap. (Make sure to check the box "Install Npcap with winpcap compatibility mode" during setup).

Linux: Usually pre-installed. If missing, run sudo apt install libpcap-dev.

macOS: Built-in natively.

2. Python Libraries
Install the necessary Python packages using pip:

Bash
pip install scapy mac-vendor-lookup flask
Running the Application
Because this script manipulates low-level network packets, you must execute it with administrative/root privileges.

Windows
Open Command Prompt or PowerShell as Administrator.

Navigate to your project directory and run:

DOS
python app.py
Linux / macOS
Open your terminal.

Navigate to your project directory and execute using sudo:

Bash
sudo python app.py
Accessing the Dashboard
Once the terminal displays [+] Admin privileges confirmed. Starting local server..., open your web browser and go to:

Plaintext
http://127.0.0.1:5000
Your local network range will be automatically suggested in the input box. Click Scan Network to refresh the view with active network targets.

## Usage

```bash
python3 app.py
```

