import socket
import json
import os
import platform
import ctypes

def is_admin():
    """Checks if the script is running with Administrator/Root privileges."""
    try:

        if platform.system() == "Windows":
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        else:
            return os.geteuid() == 0
        
    except Exception:
        return False

def get_local_subnet():
    """Detects the local IP and returns it formatted as a /24 subnet."""
    local_ip = ""
    
    try:

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
    except Exception:
        try:

            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
        except Exception:

            local_ip = "127.0.0.1" 

    ip_parts = local_ip.split('.')
    return f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"

def save_to_json(data, filename="network_devices.json"):
    """Saves a Python dictionary/list to a formatted JSON file."""
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)