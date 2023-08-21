"""1615. Maximal Network Rank
https://leetcode.com/problems/maximal-network-rank/
"""
from typing import List
import collections


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        ans = 0
        for i in range(n):
            for j in range(n):
                if j != i:
                    ans = max(ans, len(graph[i]) + len(graph[j]) - (1 if i in graph[j] else 0))
        return ans
