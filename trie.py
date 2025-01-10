class Trie:
    def __init__(self):
        self._root = {}

    def put(self, word: str, value: int) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        if not word:
            raise ValueError("Word cannot be empty")

        current = self._root

        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]

        current['*'] = value

    def get(self, word: str) -> int:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")

        current = self._root

        for char in word:
            if char not in current:
                return None
            current = current[char]

        return current.get('*')

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
