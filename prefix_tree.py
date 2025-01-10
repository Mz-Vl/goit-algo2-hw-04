from trie import Trie
from typing import Dict, List

class Homework(Trie):
    def _collect_words(self, node: Dict, current_word: str) -> List[str]:
        words = []
        if '*' in node:
            words.append(current_word)

        for char, child in node.items():
            if char != '*':
                words.extend(self._collect_words(child, current_word + char))
        return words

    def get_all_words(self) -> List[str]:
        return self._collect_words(self._root, "")

    def count_words_with_suffix(self, pattern: str) -> int:
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string")
        if not pattern:
            raise ValueError("Pattern cannot be empty")

        all_words = self._collect_words(self._root, "")
        return sum(1 for word in all_words if word.endswith(pattern))

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")
        if not prefix:
            raise ValueError("Prefix cannot be empty")

        current = self._root

        for char in prefix:
            if char not in current:
                return False
            current = current[char]

        def has_word(node: Dict) -> bool:
            if '*' in node:
                return True
            return any(has_word(child) for char, child in node.items() if char != '*')

        return has_word(current)


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    # Виведення всіх слів у дереві
    print("Words in the tree:")
    words_in_trie = trie.get_all_words()
    print(words_in_trie)