class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def all_words(self):
        def _dfs(node, prefix, words):
            if node.is_end:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)
        words = []
        _dfs(self.root, "", words)
        return words

if __name__ == "__main__":
    words = ["cachorro", "carro", "casa", "computador", "cadeira", "caneta", "camisa", "caderno", "cartão", "chuva"]
    trie = Trie()
    for word in words:
        trie.insert(word)
    print(trie.all_words())
