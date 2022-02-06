"""802. Find Eventual Safe States
https://leetcode.com/problems/find-eventual-safe-states/
"""
from typing import List


def eventual_safe_nodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    color = [0] * n  # 0: not visited; 1: visited; 2: safe point

    def safe(x: int) -> bool:
        if color[x] > 0:
            return color[x] == 2
        color[x] = 1
        for y in graph[x]:
            if not safe(y):
                return False
        color[x] = 2
        return True

    return [i for i in range(n) if safe(i)]
