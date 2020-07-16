"""785. Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/
"""
from typing import List


class Solution:
    def is_bipartite(self, graph: List[List[int]]) -> bool:
        def mark(idx: int, flag: int):
            nonlocal ans
            marked[idx] = flag
            for point in graph[idx]:
                if marked[point] == flag:
                    ans = False
                    return
                if marked[point] == 0:
                    mark(point, -flag)

        n = len(graph)
        marked = [0] * n  # 0 unmarked, 1 marked a, -1 marked b
        ans = True
        for i in range(n):
            if marked[i] == 0:
                mark(i, 1)
                if not ans:
                    return False
        return True
