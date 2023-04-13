"""2017. Grid Game
https://leetcode.cn/problems/grid-game
"""
from typing import List


class Solution:
    def grid_game(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        for i in range(2):
            for j in range(1, n):
                grid[i][j] += grid[i][j - 1]
        ans = 5000000001
        for i in range(n):
            a = grid[0][-1] - grid[0][i]
            b = grid[1][i - 1] if i > 0 else 0
            ans = min(ans, max(a, b))
        return ans
