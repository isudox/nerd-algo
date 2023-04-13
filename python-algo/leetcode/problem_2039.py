"""2039. The Time When the Network Becomes Idle
https://leetcode.com/problems/the-time-when-the-network-becomes-idle/
"""
import collections
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        def helper(x: int, cost: int):
            dist[x] = min(dist[x], cost)
            visited[x] = True
            for y in graph[x]:
                if visited[y]:
                    continue
                helper(y, cost + 1)
            visited[x] = False

        n = len(patience)
        visited = [False] * n
        visited[0] = True
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        dist = [n] * n
        helper(0, 0)
        ans = 0
        for i in range(1, n):
            time = dist[i] * 2
            if time > patience[i]:
                recent_time = time - 1
                while recent_time % patience[i] != 0:
                    recent_time -= 1
                time += recent_time
            ans = max(ans, time)
        return ans + 1
