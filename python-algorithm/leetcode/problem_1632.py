"""1632. Rank Transform of a Matrix
https://leetcode.com/problems/rank-transform-of-a-matrix/
"""
import collections
from typing import List


class Solution:
    def matrix_rank_transform(self, matrix: List[List[int]]) -> List[List[int]]:
        def find(x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        m, n = len(matrix), len(matrix[0])
        rank = [0] * (m + n)
        store = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                store[matrix[i][j]].append((i, j))
        for v in sorted(store):
            uf = list(range(m + n))
            temp_rank = rank[:]
            for i, j in store[v]:
                i, j = find(i), find(j + m)
                uf[i] = j
                temp_rank[j] = max(temp_rank[i], temp_rank[j])
            for i, j in store[v]:
                rank[i] = rank[j + m] = matrix[i][j] = temp_rank[find(i)] + 1
        return matrix
