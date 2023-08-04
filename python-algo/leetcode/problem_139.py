"""139. Word Break
https://leetcode.com/problems/word-break/
"""
from typing import List
import functools


class Solution:

    def word_break_1(self, s: str, word_dict: List[str]) -> bool:
        unmatched = set()

        def backtrack(string: str) -> bool:
            if string in unmatched:
                return False
            for word in word_dict:
                if string == word:
                    return True
                if string.startswith(word):
                    if backtrack(string[len(word):]):
                        return True
            unmatched.add(string)
            return False

        return backtrack(s)

    def word_break_2(self, s: str, word_dict: List[str]) -> bool:
        visited = {}

        def backtrack(cur_str: str) -> bool:
            if cur_str in visited:
                return visited[cur_str]
            if cur_str in word_dict:
                return True
            for i in range(1, len(cur_str)):
                if cur_str[:i] in word_dict and backtrack(cur_str[i:]):
                    visited[cur_str] = True
                    return True
                i += 1
            visited[cur_str] = False
            return False

        return backtrack(s)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @functools.cache
        def dfs(i: int, pre: str) -> bool:
            cur = pre + s[i]
            if i == len(s) - 1:
                return cur in wordDict
            if cur in wordDict:
                if dfs(i + 1, ''):
                    return True
            return dfs(i + 1, cur)

        wordDict = set(wordDict)
        return dfs(0, '')
