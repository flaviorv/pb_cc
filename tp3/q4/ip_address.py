from ipaddress import IPv4Address, IPv4Network
ip = "192.168.1.5"
network = "192.168.1.0/24"

print(f"The ip {ip} is in network {network}: {IPv4Address("192.168.1.5") in IPv4Network("192.168.1.0/24")}")

