"""802. Find Eventual Safe States
https://leetcode.com/problems/find-eventual-safe-states/
"""
from typing import List


class Solution:
    def eventual_safe_nodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(x: int) -> bool:
            if color[x] > 0:
                return color[x] == 2
            color[x] = 1
            for y in graph[x]:
                if not dfs(y):
                    return False
            color[x] = 2
            return True

        n = len(graph)
        color = [0] * n  # 0: not visited; 1: visited; 2: safe point
        return [i for i in range(n) if dfs(i)]
