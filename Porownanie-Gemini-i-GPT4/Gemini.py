import scapy.all as scapy

def scan_ip(ip):
    # Spróbuj nawiązać połączenie HTTP
    response = scapy.send(scapy.IP(dst=ip)/scapy.TCP(dport=80), verbose=False)
    if response:
        if b"HTTP" in response[0][TCP].data:
            print(f"Found camera at {ip}: HTTP")
            return True

    # Spróbuj nawiązać połączenie RTSP
    response = scapy.send(scapy.IP(dst=ip)/scapy.UDP(dport=554), verbose=False)
    if response:
        if b"RTSP" in response[0][UDP].data:
            print(f"Found camera at {ip}: RTSP")
            return True

    return False

if __name__ == "__main__":
    for ip in range(83251280, 832525526):
        scan_ip(scapy.utils.inet_ntoa(ip))
