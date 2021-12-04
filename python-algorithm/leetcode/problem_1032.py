"""1032. Stream of Characters
https://leetcode.com/problems/stream-of-characters/
"""
import collections
from typing import List


class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def has_prefix(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch in node.children:
                if node.children[ch].end:
                    return True
                node = node.children[ch]
            else:
                return False
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = ''
        self.trie = Trie()
        for word in words:
            self.trie.add(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream = letter + self.stream
        return self.trie.has_prefix(self.stream)
