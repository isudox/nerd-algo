"""472. Concatenated Words
https://leetcode.com/problems/concatenated-words/
"""
import collections
import functools
from typing import List


class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.end = False

    def insert(self, word: str):
        node = self
        for ch in word:
            idx = ord(ch) - 97
            if idx not in node.children:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.end = True

    @functools.lru_cache(None)
    def search(self, word: str, pos: int) -> bool:
        if pos >= len(word):
            return True
        node = self
        for i in range(pos, len(word)):
            pos = ord(word[i]) - 97
            if pos not in node.children:
                return False
            node = node.children[pos]
            if node.end and self.search(word, i + 1):
                return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        words.sort(key=len)
        root = Trie()
        for word in words:
            if word == '':
                continue
            if root.search(word, 0):
                ans.append(word)
            else:
                root.insert(word)
        return ans
