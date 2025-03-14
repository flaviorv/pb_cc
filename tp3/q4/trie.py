import time, ipaddress
from random import randrange

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, ip):
        ip = self.convert_ipv6_to_binary(ip)
        node = self.root
        for char in ip:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def longest_prefix_match(self, prefix):
        prefix = self.convert_ipv6_to_binary(prefix)
        response = ""
        node = self.root
        iterations = 0
        for char in prefix:
            iterations+=1
            if char not in node.children:
                if response == "":
                    return response, iterations
                continue
            response+=char
            node = node.children[char]
        while node.is_end == False:
            iterations+=1
            keys = list(node.children.keys())
            response+=keys[0]
            node = node.children[keys[0]]
        return response, iterations

    def convert_ipv6_to_binary(self, prefix):
        try:
            net_obj = ipaddress.ip_network(prefix, strict=False)
            if isinstance(net_obj, ipaddress.IPv6Network):
                return bin(int(net_obj.network_address))[2:].zfill(128)
            return prefix
        except ValueError:
            try:
                ip_obj = ipaddress.ip_address(prefix)
                if isinstance(ip_obj, ipaddress.IPv6Address):
                    return bin(int(ip_obj))[2:].zfill(128)
                return prefix
            except ValueError:
                return prefix

def linear_longest_prefix_match(prefixes, ipv4):
    response = ""
    best_match = 0
    iterations = 0
    for prefix in prefixes:
        min_len = min(len(prefix), len(ipv4))
        count = 0
        for i in range(min_len):
            iterations+=1
            if prefix[i] == ipv4[i]:
                count +=1
        if count > best_match:
            best_match = count
            response = prefix
    return response, iterations


if __name__ == "__main__":
    trie = Trie()
    networks = ["2001:db8::/32", "2001:db8:1234::/48", "192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8"]
    for network in networks:
        trie.insert(network)
    ipv6 = "2001:db8:1234:5678::1"
    response, iterations = trie.longest_prefix_match(ipv6)
    print(f"Trie longest prefix match of {ipv6}: {response if response else "Not found"}")
    ipv4 = "192.168.1.100"
    response, iterations = trie.longest_prefix_match(ipv4)
    print(f"Trie longest prefix match of {ipv4}: {response if response else "Not found"}")

    ipv4_trie = Trie()
    ipv4_networks = []
    for _ in range(1000):
        ip = f"{randrange(0, 256)}.{randrange(0, 256)}.{randrange(0, 256)}.{randrange(0, 256)}"
        prefix = randrange(24, 31)
        network = str(ipaddress.ip_network(f"{ip}/{prefix}", strict=False))
        ipv4_networks.append(network)
        ipv4_trie.insert(network)

    ipv4 = "192.168.200"
    start = time.time()
    response, iterations = ipv4_trie.longest_prefix_match(ipv4)
    print(f"Trie longest prefix match of {ipv4}: {response if response else "Not found"} Time: {round((time.time() - start), 3)} seconds Iterations: {iterations}")
    start = time.time()
    response, iterations = linear_longest_prefix_match(ipv4_networks, ipv4)
    print(f"Linear longest prefix match of {ipv4}: {response if response else "Not found"} Time: {round((time.time() - start), 3)} seconds Iterations: {iterations}")
