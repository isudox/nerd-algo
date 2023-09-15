"""2596. Check Knight Tour Configuration
https://leetcode.com/problems/check-knight-tour-configuration/
"""
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        n = len(grid)
        store = [(0, 0) for _ in range(n * n)]
        for i in range(n):
            for j in range(n):
                store[grid[i][j]] = (i, j)
        for i in range(1, n * n):
            x, y = store[i]
            px, py = store[i - 1]
            if abs((x - px) * (y - py)) != 2:
                return False
        return True
