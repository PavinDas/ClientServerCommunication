from scapy.all import ARP, Ether, srp
import re
from collections import defaultdict

def scan_network(ip_range):
    arp_request = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp_request

    result = srp(packet, timeout=2, verbose=0)[0]

    active_hosts = []
    for sent, received in result:
        active_hosts.append({'ip': received.psrc, 'mac': received.hwsrc})

    return active_hosts


def parse_log_file(log_file_path):
    log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*\] "(?P<request>.*)"')

    ip_count = defaultdict(int)
    request_count = defaultdict(int)

    with open(log_file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                ip = match.group('ip')
                request = match.group('request')
                ip_count[ip] += 1
                request_count[request] += 1

    return ip_count, request_count

ip_range = "192.168.1.1/24" 
print("Scanning network for active hosts...")
active_hosts = scan_network(ip_range)
print("Active hosts:")
for host in active_hosts:
    print(f"IP: {host['ip']}, MAC: {host['mac']}")
# Simulate log analysis
log_file_path = "network_logs.txt"
print("\nAnalyzing network logs...")
ip_count, request_count = parse_log_file(log_file_path)
print("IP Address Counts:")
for ip, count in ip_count.items():
    print(f"{ip}: {count} requests")
print("\nRequest Counts:")
for request, count in request_count.items():
    print(f"Request '{request}': {count} occurrences")