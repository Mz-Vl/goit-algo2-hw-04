class Trie:
    def __init__(self):
        self._root = {}

    def put(self, word: str, value: int) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        if not word:
            raise ValueError("Word не cannot be empty")

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