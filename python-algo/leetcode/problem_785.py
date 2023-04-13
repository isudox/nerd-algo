"""785. Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/
"""
from typing import List


class Solution:
    def is_bipartite(self, graph: List[List[int]]) -> bool:
        def dfs(x: int, flag: int) -> bool:
            groups[x] = flag
            for y in graph[x]:
                if groups[y] == flag:
                    return False
                if groups[y] == 0:
                    if not dfs(y, -flag):
                        return False
            return True

        n = len(graph)
        groups = [0] * n  # 0 ungrouped, 1: group A, -1: group B
        for i in range(n):
            if groups[i] == 0:
                if not dfs(i, 1):
                    return False
        return True
