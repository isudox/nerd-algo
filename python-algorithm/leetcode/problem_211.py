"""211. Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""
import collections


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def add_word(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


class Trie:
    def __init__(self):
        self.kids = collections.defaultdict(Trie)
        self.end = False

    def insert(self, word: str):
        cur = self
        for ch in word:
            if not cur.kids[ch]:
                cur.kids[ch] = Trie()
            cur = cur.kids[ch]
        cur.end = True

    def search(self, pattern: str) -> bool:
        cur = self
        for i, ch in enumerate(pattern):
            if ch == '.':
                for _, kid in cur.kids.items():
                    if kid.search(pattern[i + 1:]):
                        return True
                return False
            else:
                if not cur.kids[ch]:
                    return False
                cur = cur.kids[ch]
        return cur.end
