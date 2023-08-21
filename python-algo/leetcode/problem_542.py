"""542. 01 Matrix
https://leetcode.com/problems/01-matrix/
"""
from typing import List
import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = collections.deque()
        MAX = m * n + 1
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = MAX
        while q:
            i, j = q.popleft()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] > mat[i][j] + 1:
                    q.append((ni, nj))
                    mat[ni][nj] = mat[i][j] + 1
        return mat

