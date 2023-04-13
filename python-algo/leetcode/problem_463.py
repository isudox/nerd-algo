"""463. Island Perimeter
https://leetcode.com/problems/island-perimeter/

You are given row x col grid representing a map where grid[i][j] = 1
represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island
(i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to
the water around the island. One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4

Constraints:

    row == grid.length
    col == grid[i].length
    1 <= row, col <= 100
    grid[i][j] is 0 or 1.
"""
from typing import List


class Solution:
    def island_perimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(grid), len(grid[0])
        moves = [[0, -1], [-1, 0]]  # only check left and upside.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                ans += 4
                for move in moves:
                    prev_row, prev_col = row + move[0], col + move[1]
                    if 0 <= prev_row < rows and 0 <= prev_col < cols:
                        if grid[prev_row][prev_col] == 1:
                            ans -= 2
        return ans
