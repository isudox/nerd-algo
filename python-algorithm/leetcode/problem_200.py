"""200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid
are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
from typing import List


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, col: int):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
