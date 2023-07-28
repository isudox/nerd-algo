"""
https://leetcode.com/problems/parallel-courses-iii/
"""
import functools
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        @functools.cache
        def dfs(x: int) -> int:
            ret = 0
            for p in prev[x]:
                ret = max(ret, dfs(p))
            ret += time[x - 1]
            return ret

        ans = 0
        prev = [[] for _ in range(n + 1)]
        for a, b in relations:
            prev[b].append(a)
        for i in range(1, n + 1):
            ans = max(ans, dfs(i))
        return ans
