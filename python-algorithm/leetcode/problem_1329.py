"""1329. Sort the Matrix Diagonally
https://leetcode.com/problems/sort-the-matrix-diagonally/
"""
import collections
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0]),
        d = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i - j].append(mat[i][j])
        for i in d:
            d[i].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i - j].pop()
        return mat
