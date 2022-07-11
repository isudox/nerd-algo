"""676. Implement Magic Dictionary
https://leetcode.com/problems/implement-magic-dictionary/
"""
from typing import List


class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for d in dictionary:
            self.trie.add(d)

    def search(self, searchWord: str) -> bool:
        return self.trie.search(searchWord, False)


class Trie:

    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word: str) -> None:
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.end = True

    def search(self, word: str, changed: bool) -> bool:
        cur = self
        for i, ch in enumerate(word):
            if ch not in cur.children:
                if changed:
                    return False
                for nxt in cur.children:
                    if cur.children[nxt].search(word[i + 1:], True):
                        return True
                return False
            elif changed:
                cur = cur.children[ch]
            else:
                for nxt in cur.children:
                    if cur.children[nxt].search(word[i + 1:], False if nxt == ch else True):
                        return True
                return False
        if not changed:
            return False
        if not cur.end:
            return False
        return True
