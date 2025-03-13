class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_prefix = False
        self.prefix = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, cidr):
        ip, prefix_length = cidr.split('/')
        prefix_length = int(prefix_length)
        binary_ip = self._ip_to_binary(ip)[:prefix_length]
        node = self.root
        for bit in binary_ip:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.is_end_of_prefix = True
        node.prefix = cidr

    def longest_prefix_match(self, ip):
        binary_ip = self._ip_to_binary(ip)
        node = self.root
        longest_match = None
        for bit in binary_ip:
            if bit in node.children:
                node = node.children[bit]
                if node.is_end_of_prefix:
                    longest_match = node.prefix
            else:
                break
        return longest_match

    def _ip_to_binary(self, ip):
        return '.'.join(f'{int(octet):08b}' for octet in ip.split('.'))

if __name__ == "__main__":
	trie = Trie()
	trie.insert("192.168.0.0/16")
	trie.insert("192.168.1.0/24")
	trie.insert("10.0.0.0/8")
	ip = "192.168.1.100"
	print(f"The longest prefix match of ip {ip} is: {trie.longest_prefix_match(ip)}")
