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
        return self.trie.search(searchWord)


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

    def search(self, word: str, cnt: bool) -> bool:
        cur = self
        for i, ch in enumerate(word):
            if ch not in cur.children:
                if not cnt:
                    return False
                cnt = True
                for nxt in cur.children:
                    cur = cur.children[nxt]
                    if cur.search(word[i + 1:], True):
                        return True
                return False
            else:
                cur = cur.children[ch]
        if cnt == 1:
            return False
        if not cur.end:
            return False
        return True
