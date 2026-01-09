from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

LOG_FILE = "packets.log"

def log_line(text: str) -> None:
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()} {text}\n")
                
def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst

        proto = "OTHER"
        sport = dport = ""

        if TCP in packet:
            proto = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif UDP in packet:
            proto = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
        
        print(f"{proto}{src}:{sport} -> {dst}:{dport}")
        log_line(f"{proto} {src}:{sport} -> {dst}:{dport}")

def main():
    print("Starting packet sniffer... (Ctrl+C to stop)")
    sniff(prn=packet_callback, store=False, filter="tcp port 443")

if __name__ == "__main__":
    main()