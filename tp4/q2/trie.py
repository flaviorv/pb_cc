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

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def matches(self, prefix):
        response = ""
        all = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return "Not found"
            response+=char
            if node.is_end == True:
                all.append(response)
            node = node.children[char]
        self.after_match(node, response, all)
        return all

    def after_match(self, node, response, all):
        matched = response
        keys = list(node.children.keys())
        if node.is_end == True:
            all.append(response)
        for i in range(len(keys)):
            response += keys[i]
            self.after_match(node.children[keys[i]], response, all)
            response = matched

if __name__ == "__main__":
    words = ["apple", "apricot", "autocomplete", "best", "banana", "basket", "car", "cat",
        "dog", "door", "elephant", "engine", "engineer", "island", "jacket", "keyboard", "house"]

    trie = Trie()
    for word in words:
        trie.insert(word)
    i = 1
    print(f"Words: {trie.all_words()}")
    while i != "0":
        i = str(input("Type a prefix to autocomplete or 0 to exit: "))
        print(f"Matches: {trie.matches(i)}")
        print()
