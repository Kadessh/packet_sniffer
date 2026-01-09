Packet Sniffer & Network Analyzer
A simple Python-based network packet sniffer built using Scapy
     
     Overview

This project is a Python-based packet sniffer that captures live network traffic, analyzes it, and displays useful information such as:
    - Source & destination IP addresses
    - TCP/UDP ports
    - Transport protocol (TCP/UDP/Other)
    - Real-time packet summaries
    - Optional logging to file
It is built using Scapy, one of the most powerful network-analysis libraries in Python.

This tool is part of my cybersecurity learning roadmap focusing on networking fundamentals, packet analysis, and low-level traffic inspection.

     Features

- Live packet capture
    Captures packets from the active network interface in real time.
- Protocol detection
    Identifies whether each packet contains:
        . TCP
        . UDP
        . Other protocols (ICMP, ARP, etc. optional)
- Source/Destination info 
    Extracts:
        . IP → Source & Destination
        . Ports → Source & Destination (for TCP/UDP)
- BPF Filtering support
    Allows filters such as:
        . tcp
        . udp
        . port 80
        . tcp port 443
        . host 8.8.8.8
- Optional file logging
    All captured packets can be logged with timestamps.

     Technologies Used

. Python 3
. Scapy
. macOS (but works on Linux too)

    Project Structure

packet_sniffer/
│
├── sniffer.py        # main packet sniffing script
├── packets.log        # optional log file (auto-created)
└── README.md          # documentation

    Installation

1. Clone the repository
    git clone https://github.com/<your-username>/packet_sniffer.git
    cd packet_sniffer

2. Install dependencies
    python3 -m pip install scapy

     Usage

Run the sniffer (macOS/Linux requires sudo):
    sudo python3 sniffer.py

You should see output like:
    TCP 192.168.1.14:52932 -> 142.251.32.131:443
    UDP 192.168.1.14:5353 -> 224.0.0.251:5353

Stop with:
    Ctrl + C

     Filtering Traffic

You can specify a filter (optional):
    Example: 
    Show only TCP traffic:
        sniff(filter="tcp", prn=packet_callback, store=False)
    
    Show only UDP traffic:
        sniff(filter="udp", prn=packet_callback, store=False)

    Show HTTPS traffic:
        sniff(filter="tcp port 443", prn=packet_callback, store=False)

     Logging (Optional)

The script can log every packet to a file (packets.log):
    Example log entry:
        2025-01-12T14:22:10 TCP 192.168.1.10:52932 -> 142.251.32.131:443

    Great for:
        - Post-analysis
        - Intrusion-detection logic
        - Auditing traffic over long periods

     How It Works (Short Explanation)

The script uses Scapy’s sniff() function to capture packets.
Every captured packet is passed to packet_callback().
The callback checks for IP, TCP, and UDP layers.
It extracts:
    . src and dst
    . sport and dport
It prints a clean summary in the terminal.
If logging is enabled, it writes the same info to packets.log.

     Why This Matters 

Packet sniffing is a fundamental skill in cybersecurity because it teaches:
    - How traffic flows across networks
    - How transport layer protocols behave
    - How attackers analyze or intercept traffic
    - How intrusion detection systems work
    - How ports/services communicate

This project forms the foundation for:

    - Network intrusion detection systems (NIDS)
    - Traffic classifiers
    - Port scanners
    - Firewall development
    - Malware traffic analysis

     Future Improvements

Planned enhancements:
    - Add command-line arguments (--filter, --log, --iface)
    - Add packet counting & statistics summary
    - Detect suspicious patterns (port scans, repeated SYNs)
    - Add colored terminal output for readability
    - Save capture as .pcap file
    - Build a simple GUI dashboard

     Author

Kadesh Folusho Yahaya
Email: <kadeshyahaya@gmail.com>
GitHub: <https://github.com/Kadessh>