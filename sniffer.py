import scapy.all as scapy

def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        proto = packet[scapy.IP].proto
        
        print(f"[+] Packet: {src_ip} ----> {dst_ip} | Protocol: {proto}")
        
        # If it contains raw data/payload, print it
        if packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load
            print(f"    [Raw Data]: {payload}\n")

def start_sniffing(interface=None):
    print("[*] Starting Network Sniffer... Press Ctrl+C to stop.")
    # Sniffing packets, store=False means don't keep them in memory
    scapy.sniff(iface=interface, store=False, prn=packet_callback)

if __name__ == "__main__":
    # You can specify an interface like 'eth0' or 'wlan0', or leave it None for default
    start_sniffing()
