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

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end:
                    print(f"{word} not found to be removed")
                    return False
                node.is_end = False
                print(f"{word} removed")
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                print(f"{word} not found to be removed")
                return False
            should_delete_child = _delete(node.children[char], word, depth + 1)
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end
            return False
        _delete(self.root, word, 0)

if __name__ == "__main__":
    words = ["apple", "apricot", "autocomplete", "best", "banana", "basket", "car", "cat", "cap"
        "dog", "door", "elephant", "engine", "engineer", "island", "jacket", "keyboard", "house"]

    trie = Trie()
    for word in words:
        trie.insert(word)
    print(f"Words: {trie.all_words()}")
    word = "apple"
    print(f"Is {word} in the trie:", trie.search(word))
    word = "computer"
    print(f"Is {word} in the trie:", trie.search(word))
    prefixes = ["ap", "a", "ba", "ho", "aa", "ca"]
    for prefix in prefixes:
        print(f"Autocomplete of {prefix}: {trie.matches(prefix)}")
    trie.delete("apple")
    trie.delete("a")
    trie.delete("doorr")
    prefix = "ap"
    print(f"Autocomplete of {prefix}: {trie.matches(prefix)}")
