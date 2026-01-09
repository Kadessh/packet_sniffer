import argparse
from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP

LOG_FILE = "packets.log"

def log_packet(log_file: str, text: str) -> None:
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()} {text}\n")
                
def packet_callback(packet, log_file=None):
    if IP not in packet:
        return
    
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
        
    line = f"{proto} {src}:{sport} -> {dst}:{dport}"
    print(line)

    if log_file:
        log_packet(log_file, line)

def main():
    parser = argparse.ArgumentParser(
        description="Python Packet Sniffer using Scapy"
    )

    parser.add_argument(
        "--filter",
        help="BPF filter string (e.g. 'tcp', 'tcp port 443')",
        default=None
    )

    parser.add_argument(
        "--iface",
        help="Network interface to sniff on (e.g. en0)",
        default=None
    )

    parser.add_argument(
        "--log",
        help="Log packets to a file",
        default=None
    )

    parser.add_argument(
        "--count",
        help="Stop after capturing N packets",
        type=int,
        default=0
    )

    args = parser.parse_args()

    print("Starting packet sniffer...")
    if args.filter:
        print(f"Filter: {args.filter}")
    if args.iface:
        print(f"Interface: {args.iface}")
    if args.log:
        print(f"Logging to: {args.log}")
    if args.count:
        print(f"Packet count limit: {args.count}")

    sniff(
        iface=args.iface,
        filter=args.filter,
        prn=lambda pkt: packet_callback(pkt, args.log),
        store=False,
        count=args.count if args.count > 0 else 0
    )

if __name__ == "__main__":
    main()