from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup

mac_lookup = MacLookup()

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
            
        devices.append({
            "ip": ip_address,
            "mac": mac_address,
            "vendor": vendor
        })
        
    return devices

if __name__ == "__main__":
    target_ip = "192.168.1.1/24" 
    
    found_devices = scan_network(target_ip)
    
    print("\nIP Address\t\tMAC Address\t\tVendor")
    print("-" * 65)
    for device in found_devices:
        print(f"{device['ip']}\t\t{device['mac']}\t{device['vendor']}")