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
from typing import List


class Solution:
    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        def find(point: int) -> int:
            if parent[point] != point:
                parent[point] = find(parent[point])
            return parent[point]

        def union(p1: int, p2: int):
            parent[find(p1)] = find(parent[p2])

        n = len(edges)
        parent = [_ for _ in range(n + 1)]
        for edge in edges:
            if find(edge[0]) != find(edge[1]):
                union(edge[0], edge[1])
            else:
                return edge
        return []
