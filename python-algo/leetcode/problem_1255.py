"""1255. Maximum Score Words Formed by Letters
https://leetcode.com/problems/maximum-score-words-formed-by-letters/
"""
import collections
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def dfs(i: int, total: int) -> None:
            if i >= len(words):
                nonlocal ans
                ans = max(ans, total)
                return
            dfs(i + 1, total)
            for j, c in enumerate(words[i]):
                if store[c] == 0:
                    for x in words[i][:j]:
                        store[x] += 1
                    return
                store[c] -= 1
                total += score[ord(c) - 97]
            dfs(i + 1, total)
            for c in words[i]:
                store[c] += 1

        store = collections.Counter(letters)
        ans = 0
        dfs(0, 0)
        return ans
