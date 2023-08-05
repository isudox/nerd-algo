"""980. Unique Paths III
https://leetcode.com/problems/unique-paths-iii/
"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def backtrack(x: int, y: int, cnt: int):
            if x == ex and y == ey:
                if cnt != moves:
                    return
                nonlocal ans
                ans += 1
                return
            grid[x][y] = 9
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (grid[nx][ny] == 0 or grid[nx][ny] == 2):
                    backtrack(nx, ny, cnt + 1)
            grid[x][y] = 0

        sx = sy = ex = ey = 0
        moves = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    continue
                if grid[i][j] == 0:
                    moves += 1
                elif grid[i][j] == 1:
                    sx, sy = i, j
                else:
                    ex, ey = i, j
        ans = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        backtrack(sx, sy, 0)
        return ans
