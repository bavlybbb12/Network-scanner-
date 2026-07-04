Python Network Scanner
A lightweight, Python-based network scanning tool that uses the Address Resolution Protocol (ARP) to discover active devices on a local area network (LAN). It retrieves IP addresses, MAC addresses, resolves the hardware manufacturer (vendor), and exports the results to a structured JSON file.

Features
ARP Discovery: Broadcasts ARP requests at Layer 2 to accurately identify active devices on the subnet.

MAC Vendor Resolution: Automatically looks up the manufacturer of the discovered network interface cards.

JSON Export: Saves scan results into a formatted network_devices.json file for historical logging or integration with other applications.

Terminal Output: Prints a clean, tab-separated table of discovered devices directly to the console.

Prerequisites
This script requires Python 3.x and the following system-level driver for packet manipulation:

Windows Users: You must install Npcap to allow Scapy to send and sniff packets at Layer 2.

Download it from npcap.com.

During installation, ensure you check the box for "Install Npcap in WinPcap API-compatible Mode".

Installation
Clone or download this repository to your local machine.

Open your terminal or command prompt in the project directory.

Install the required Python libraries using pip:

Bash
pip install scapy mac-vendor-lookup
Usage
Open scanner.py in your code editor.

Scroll to the bottom of the script and locate the target_ip variable in the execution block.

Update this variable to match your local network's subnet (e.g., 192.168.1.1/24, 10.0.0.1/24, etc.).

Python
if __name__ == "__main__":
    # Update this to match your actual network subnet
    target_ip = "192.168.1.1/24" 
Run the script from your terminal:

Bash
python scanner.py
Output
The script will output a table of found devices to your terminal:

Plaintext
Scanning 192.168.1.1/24...

IP Address              MAC Address             Vendor
-----------------------------------------------------------------
192.168.1.1             a1:b2:c3:d4:e5:f6       Cisco Systems, Inc
192.168.1.15            12:34:56:78:90:ab       Apple, Inc.
It will also automatically generate a file named network_devices.json in the same directory, structured like this:

JSON
[
    {
        "ip": "192.168.1.1",
        "mac": "a1:b2:c3:d4:e5:f6",
        "vendor": "Cisco Systems, Inc"
    },
    {
        "ip": "192.168.1.15",
        "mac": "12:34:56:78:90:ab",
        "vendor": "Apple, Inc."
    }
]

Future Roadmap
This project is actively being developed. Below is a detailed breakdown of planned features and upgrades that will transform this script from a simple command-line tool into a comprehensive network management dashboard.

1. Web-Based Dashboard (Flask Integration)
Transitioning the terminal output to an interactive, browser-based graphical user interface (GUI).

Local Web Server: Utilize Flask to serve a lightweight local application.

Dynamic Frontend: Use HTML, CSS, and Bootstrap/Tailwind to create a clean, responsive table that automatically loads data from the network_devices.json file.

Trigger Scans via UI: Add a "Scan Network" button on the dashboard that triggers the backend Python script and refreshes the page with the latest data without needing to touch the terminal.

2. Continuous Monitoring & Alerting
Upgrading the script to run as a background service (daemon) to act as a localized Intrusion Detection System (IDS).

Historical Database: Shift from a single JSON overwrite to appending scans, creating a historical log of when specific devices join or leave the network.

Rogue Device Detection: Implement logic to compare current scan results against a "whitelist" of known MAC addresses.

Automated Alerts: Integrate webhooks (like Discord, Slack, or simple Email SMTP) to instantly notify the network admin if an unrecognized or unauthorized MAC address connects to the subnet.

3. Layer 4 Port Scanning
Expanding the scanner's capabilities beyond Layer 2 (ARP) discovery to actively probe discovered devices for open communication ports.

Socket Connections: Use Python's built-in socket library to attempt connections on common ports (e.g., 22 SSH, 80 HTTP, 443 HTTPS).

Service Identification: Map open ports to their associated services to get a better idea of what the device is (e.g., finding port 80 open might indicate a router's admin panel or a local web server).

Nmap Integration: Potentially wrap python-nmap into the script for deep-dive vulnerability scanning on specific target IPs.

4. Data Logging and Export Options
Enhancing how network data is stored and shared.

CSV Export: Add an option to export scan results to a .csv format for easy importing into Excel or network administration spreadsheets.

SQLite Database: Migrate from JSON files to a lightweight SQLite database for faster querying and better handling of large amounts of historical network data.