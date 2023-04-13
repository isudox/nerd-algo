"""886. Possible Bipartition
https://leetcode.com/problems/possible-bipartition/
"""
import collections
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(cur: int, group: int) -> bool:  # find if it has a cycle.
            groups[cur] = group
            for nxt in graph[cur]:
                if groups[nxt] == group:
                    return True
                if groups[nxt] == 0 and dfs(nxt, 3 - group):
                    return True
            return False

        graph = collections.defaultdict(list)
        for (a, b) in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        groups = [0] * (n + 1)
        for i in range(1, n + 1):
            if groups[i] == 0 and dfs(i, 1):
                return False
        return True
