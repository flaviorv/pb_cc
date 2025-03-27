from scapy.all import ARP, Ether, srp

network = "192.168.0.0/24"

arp_request = ARP(pdst=network)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether / arp_request
responses, _ = srp(packet, timeout=5, verbose=False)

print("Active devieces:")
for res in responses:
    print(f"IP: {res[1].psrc}, MAC: {res[1].hwsrc}")