"""1048. Longest String Chain
https://leetcode.com/problems/longest-string-chain/
"""
import collections
import functools
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        @functools.cache
        def dfs(cur: str) -> int:
            ret = 0
            for i in range(len(cur)):
                tmp = cur[0: i] + cur[i + 1:]
                if tmp in store[len(cur) - 1]:
                    ret = max(ret, dfs(tmp) + 1)
            nonlocal ans
            ans = max(ans, ret + 1)
            return ret

        ans = 0
        store = collections.defaultdict(set)
        for word in words:
            store[len(word)].add(word)
        for word in words:
            dfs(word)
        return ans
