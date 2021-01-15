"""947. Most Stones Removed with Same Row or Column
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
"""
from typing import List


class Solution:
    def remove_stones(self, stones: List[List[int]]) -> int:
        def union(x: int, y: int):
            parent[find(x)] = find(parent[y])

        def find(idx: int) -> int:
            if parent[idx] != idx:
                parent[idx] = find(parent[idx])
            return parent[idx]

        n = len(stones)
        parent = list(range(n))
        row_map = col_map = dict()
        for i in range(n):
            row, col = stones[i][0], stones[i][1]
            if row not in row_map:
                row_map[row] = i
            else:
                union(i, row_map[row])
            if col not in col_map:
                col_map[col] = i
            else:
                union(i, col_map[col])
        graphs = set()
        for i in range(n):
            graphs.add(find(i))
        return n - len(graphs)
