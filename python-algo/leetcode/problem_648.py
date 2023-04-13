"""648. Replace Words
https://leetcode.com/problems/replace-words/
"""
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda x: len(x))
        trie = Trie()
        for d in dictionary:
            trie.add(d)
        ans = []
        words = sentence.split(' ')
        for word in words:
            ret = trie.search(word)
            if ret != '':
                ans.append(ret)
            else:
                ans.append(word)
        return ' '.join(ans)


class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word: str):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.end = True

    def search(self, word: str) -> str:
        cur = self
        for i, ch in enumerate(word):
            if ch not in cur.children:
                return ''
            cur = cur.children[ch]
            if cur.end:
                return word[:i + 1]
        return word
