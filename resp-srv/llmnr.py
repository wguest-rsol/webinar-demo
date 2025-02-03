import socket
import struct
import sys
from impacket.smbconnection import SMBConnection
import time

# LLMNR multicast address and port
LLMNR_MULTICAST_ADDR = "224.0.0.252"
LLMNR_PORT = 5355

# Target name to resolve
TARGET_NAME = "ARCTIQQ"  # Change this to the target hostname

# SMB authentication details
SMB_USERNAME = "super_admin"
SMB_PASSWORD = "P@ssw0rd!"

def send_llmnr_query():
    """ Sends an LLMNR query broadcast and waits for a response """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(3)  # Wait max 3 seconds for a response

    try:
        # Join LLMNR multicast group
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                        struct.pack("=4s4s", socket.inet_aton(LLMNR_MULTICAST_ADDR), socket.inet_aton("0.0.0.0")))

        # Construct LLMNR Query Packet (Standard LLMNR Request Format)
        query_id = b"\x00\x01"  # Transaction ID
        flags = b"\x00\x00"  # Standard Query
        qdcount = b"\x00\x01"  # One question
        ancount = b"\x00\x00"  # No answers
        nscount = b"\x00\x00"  # No authority records
        arcount = b"\x00\x00"  # No additional records

        # Convert hostname to DNS-style format (length-prefixed)
        qname = b"".join([bytes([len(part)]) + part.encode() for part in TARGET_NAME.split(".")]) + b"\x00"
        qtype = b"\x00\x01"  # Type A (IPv4 Address)
        qclass = b"\x00\x01"  # Class IN (Internet)

        # Full query packet
        query_packet = query_id + flags + qdcount + ancount + nscount + arcount + qname + qtype + qclass

        # Send query to LLMNR multicast group
        sock.sendto(query_packet, (LLMNR_MULTICAST_ADDR, LLMNR_PORT))

        # Wait for response
        while True:
            try:
                data, addr = sock.recvfrom(512)  # Receive response
                if addr:
                    print(f"[+] LLMNR response received from: {addr[0]}")
                    return addr[0]  # Return the IP of the responding host
            except socket.timeout:
                print("[-] No LLMNR response received.")
                return None

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        sock.close()

def attempt_smb_auth(target_ip):
    """ Attempts SMB authentication using the given credentials """
    try:
        print(f"[+] Attempting SMB authentication to {target_ip}...")

        conn = SMBConnection(target_ip, target_ip)
        conn.login(SMB_USERNAME, SMB_PASSWORD)
        
        print("[+] SMB authentication successful!")
        conn.logoff()
    except Exception as e:
        print(f"[-] SMB authentication failed: {e}")

if __name__ == "__main__":
    while True:
        print("[*] Sending LLMNR query...")
        responder_ip = send_llmnr_query()

        if responder_ip:
            print(f"[+] Responding server: {responder_ip}")
            attempt_smb_auth(responder_ip)
        else:
            print("[-] No LLMNR responders found.")

        print("[+] Sleeping 30s.")
        time.sleep(60)
