"""2707. Extra Characters in a String
https://leetcode.com/problems/extra-characters-in-a-string/
"""
from typing import List
from functools import cache


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def dfs(pre: str, i: int) -> int:
            if i == n:
                if not pre or trie.search(pre):
                    return 0
                return len(pre)
            cur = pre + s[i]
            ret = dfs(cur, i + 1)
            if trie.search(cur):
                ret = min(ret, dfs('', i + 1))
            else:
                ret = min(ret, dfs('', i + 1) + len(cur), dfs(s[i], i + 1) + len(pre))
            return ret

        n = len(s)
        trie = Trie()
        for d in dictionary:
            trie.add(d)
        return dfs('', 0)


class Trie:
    def __init__(self, val: str = ''):
        self.val = val
        self.subs = [None] * 26
        self.end = False

    def add(self, word: str):
        cur = self
        for c in word:
            i = ord(c) - 97
            if not cur.subs[i]:
                cur.subs[i] = Trie(c)
            cur = cur.subs[i]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            i = ord(c) - 97
            if not cur.subs[i]:
                return False
            cur = cur.subs[i]
        return cur.end
