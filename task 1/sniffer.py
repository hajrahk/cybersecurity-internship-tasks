import socket
import struct

def parse_ip_header(data):
    ip_header = struct.unpack('!BBHHHBBH4s4s', data[:20])
    print("\n--- IP Header ---")
    print("Version:", ip_header[0] >> 4)
    print("Header Length:", (ip_header[0] & 15) * 4)
    print("TTL:", ip_header[5])
    print("Protocol:", ip_header[6])
    print("Source IP:", socket.inet_ntoa(ip_header[8]))
    print("Destination IP:", socket.inet_ntoa(ip_header[9]))

def sniff():
    # ✅ Step 1: Replace with your own local IP address
    HOST = "192.168.1.19"  # Example: "192.168.1.5"

    # ✅ Step 2: Create raw socket and bind to your IP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sniffer.bind((HOST, 0))

    # ✅ Step 3: Include IP headers in capture
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # ✅ Step 4: Enable promiscuous mode (Windows only)
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print("[*] Sniffer started... Press Ctrl+C to stop.\n")

    try:
        while True:
            raw_packet = sniffer.recvfrom(65565)[0]
            parse_ip_header(raw_packet)
    except KeyboardInterrupt:
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        print("\n[*] Sniffer stopped.")

sniff()
