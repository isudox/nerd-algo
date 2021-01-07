"""684. Redundant Connection
https://leetcode.com/problems/redundant-connection/

The given input is a graph that started as a tree with N nodes
(with distinct values 1, 2, ..., N),

Example 1:

Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation:
  1
 / \
2 - 3

Example 2:

Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation:
5 - 1 - 2
    |   |
    4 - 3
"""
import collections
from typing import List


class Solution:
    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        def dfs(point: int, redundant: List[List[int]]):
            if not visited[point]:
                visited[point] = True
                for next_point in graph[point]:
                    if not visited[next_point]:
                        dfs(next_point, redundant)
                    else:
                        redundant.append([point, next_point])

        n = len(edges)
        visited = [False] * (n + 1)
        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
        dfs(1, [])
        return []
