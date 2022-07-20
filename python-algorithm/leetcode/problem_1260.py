"""1260. Shift 2D Grid
https://leetcode.com/problems/shift-2d-grid/
"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                pos = (i * n + j + k) % total
                r, c = divmod(pos, n)
                ans[r][c] = grid[i][j]
        return ans
