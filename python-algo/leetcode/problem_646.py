"""646. Maximum Length of Pair Chain
https://leetcode.com/problems/maximum-length-of-pair-chain/
"""
import functools
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(idx: int) -> int:
            ret = 0
            for nxt in range(len(pairs) - 1, idx, -1):
                if pairs[nxt][0] <= pairs[idx][1]:
                    break
                ret = max(ret, dfs(nxt))
            return ret + 1

        pairs.sort(key=lambda x: (x[0], x[1]))
        ans = 0
        for i in range(len(pairs) - 1, -1, -1):
            ans = max(ans, dfs(i))
        return ans
