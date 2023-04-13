"""1443. Minimum Time to Collect All Apples in a Tree
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree
"""
import collections
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def helper(cur: int, par: int) -> int:
            if cur not in graph:
                return 0
            times = 0
            for nxt in graph[cur]:
                if nxt == par:
                    continue
                ret = helper(nxt, cur)
                if ret > 0 or hasApple[nxt]:
                    times += ret + 2
            return times

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return helper(0, -1)
