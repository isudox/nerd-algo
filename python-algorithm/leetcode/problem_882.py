"""882. Reachable Nodes In Subdivided Graph
https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
"""
import collections
import heapq
from typing import List


class Solution:
    def reachable_nodes(self, edges: List[List[int]], max_moves: int, n: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, c in edges:
            graph[u][v] = graph[v][u] = c
        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            ans += 1
            for v, c in graph[u].items():
                moves = min(c, max_moves - d)
                used[u, v] = moves
                d2 = d + c + 1
                if d2 < dist.get(v, max_moves + 1):
                    heapq.heappush(pq, (d2, v))
                    dist[v] = d2
        for u, v, c in edges:
            ans += min(c, used.get((u, v), 0) + used.get((v, u), 0))
        return ans
