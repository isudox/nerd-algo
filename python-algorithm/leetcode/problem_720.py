"""720. Longest Word in Dictionary
https://leetcode.com/problems/longest-word-in-dictionary/
"""
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        def dfs(cur: str):
            nonlocal ans
            if (len(cur) == len(ans) and cur < ans) or len(cur) > len(ans):
                ans = cur
            for i in range(26):
                ch = chr(ord('a') + i)
                next = cur + ch
                if next in store:
                    dfs(next)

        ans = ''
        store = set(words)
        for word in words:
            if len(word) == 1:
                dfs(word)
        return ans
