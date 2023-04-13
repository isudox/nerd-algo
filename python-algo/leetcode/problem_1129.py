"""1129. Shortest Path with Alternating Colors
https://leetcode.com/problems/shortest-path-with-alternating-colors/
"""
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in redEdges:
            g[u].append((v, 0))
        for u, v in blueEdges:
            g[u].append((v, 1))
        dis = [-1] * n
        vis = {(0, 0), (0, 1)}
        q = [(0, 0), (0, 1)]
        level = 0
        while q:
            sz = len(q)
            for i in range(sz):
                t = q.pop(0)
                x, color = t[0], t[1]
                if dis[x] == -1:
                    dis[x] = level
                for p in g[x]:
                    if p[1] != color and p not in vis:
                        vis.add(p)
                        q.append(p)
            level += 1
        return dis
