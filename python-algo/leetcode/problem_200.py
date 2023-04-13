"""200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid
are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

    rows == grid.length
    cols == grid[i].length
    1 <= rows, cols <= 300
    grid[i][j] is '0' or '1'.
"""
from typing import List


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        def dfs(row: int, col: int):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            grid[row][col] = '0'
            for d in dirs:
                if 0 <= row + d[0] < rows and 0 <= col + d[1] < cols and grid[row + d[0]][col + d[1]] == '1':
                    dfs(row + d[0], col + d[1])

        rows, cols = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
