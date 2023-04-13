"""1971. Find if Path Exists in Graph
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""
import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def helper(x: int, seen) -> bool:
            if x not in graph:
                return False
            if destination in graph[x]:
                return True
            seen.add(x)
            for y in graph[x]:
                if y not in seen:
                    if helper(y, seen):
                        return True
            return False

        if source == destination:
            return True
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        return helper(source, set())
