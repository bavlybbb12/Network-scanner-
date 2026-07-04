from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
import json
import socket

mac_lookup = MacLookup()

def scan_ports(ip):
    open_ports = []
    common_ports = [21, 22, 23, 80, 443, 445, 3389]
    
    for port in common_ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1) 
                
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        except Exception:
            pass
            
    return open_ports

def scan_network(ip_range):
    
    print(f"Scanning {ip_range}...")
    
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    arp_request_packet = broadcast / arp_request
    
    answered_list = srp(arp_request_packet, timeout=2, verbose=False)[0]
    
    devices = []
    
    for sent_packet, received_packet in answered_list:
        ip_address = received_packet.psrc  # psrc = source IP
        mac_address = received_packet.hwsrc # hwsrc = source hardware (MAC) address
        
        try:
            vendor = mac_lookup.lookup(mac_address)
        except Exception:
            vendor = "Unknown"
        
        active_ports = scan_ports(ip_address)
        
        devices.append({
            "ip": ip_address,
            "mac": mac_address,
            "vendor": vendor,
            "open_ports": active_ports
        })
        
    return devices

def save_to_json(data, filename="network_devices.json"):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)