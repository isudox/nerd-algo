"""1252. Cells with Odd Values in a Matrix
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
"""
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        def helper(x: int, y: int):
            for i in range(n):
                grid[x][i] += 1
            for i in range(m):
                grid[i][y] += 1

        grid = [[0] * n for _ in range(m)]
        for r, c in indices:
            helper(r, c)
        ans = 0
        for row in grid:
            for num in row:
                if num % 2 == 1:
                    ans += 1
        return ans
