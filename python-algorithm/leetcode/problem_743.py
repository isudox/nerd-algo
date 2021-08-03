"""743. Network Delay Time
https://leetcode.com/problems/network-delay-time/
"""
import collections
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dfs(node: int, duration: int):
            if duration >= path[node]:
                return
            path[node] = duration
            for time, next_node in sorted(graph[node]):
                dfs(next_node, duration + time)

        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        path = {node: float('inf') for node in range(1, n + 1)}
        dfs(k, 0)
        ans = max(path.values())
        return ans if ans < float('inf') else -1
