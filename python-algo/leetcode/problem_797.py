"""797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/
"""
from typing import List


class Solution:
    def all_paths_source_target(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(path: List[int]):
            cur = path[-1]
            if cur == n - 1:
                ans.append(path[:])
            for next_pos in graph[cur]:
                path.append(next_pos)
                dfs(path)
                path.pop()

        n = len(graph)
        ans = []
        dfs([0])
        return ans
