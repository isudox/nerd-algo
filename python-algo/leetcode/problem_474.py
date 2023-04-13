"""474. Ones and Zeroes
https://leetcode.com/problems/ones-and-zeroes/
"""
import collections
import functools
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(i: int, cnt0: int, cnt1: int) -> int:
            if i == len(strs):
                return 0
            counter = collections.Counter(strs[i])
            ret = dfs(i + 1, cnt0, cnt1)
            if cnt0 + counter['0'] <= m and cnt1 + counter['1'] <= n:
                ret = max(ret, dfs(i + 1, cnt0 + counter['0'], cnt1 + counter['1']) + 1)
            return ret

        return dfs(0, 0, 0)
