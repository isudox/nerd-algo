"""892. Surface Area of 3D Shapes
https://leetcode-cn.com/problems/surface-area-of-3d-shapes/

On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of
grid cell (i, j).

Return the total surface area of the resulting shapes.
 

Example 1:
Input: [[2]]
Output: 10

Example 2:
Input: [[1,2],[3,4]]
Output: 34

Example 3:
Input: [[1,0],[0,2]]
Output: 16

Example 4:
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

Example 5:
Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 
Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
"""
from typing import List


class Solution:
    def surface_area(self, grid: List[List[int]]) -> int:
        lines, cols = len(grid), len(grid[0])
        count = 0
        overlap = 0
        for i in range(lines):
            for j in range(cols):
                count += grid[i][j]
                overlap += grid[i][j] - 1 if grid[i][j] > 1 else 0
                if j < cols - 1:
                    overlap += min(grid[i][j], grid[i][j + 1])
        for i in range(cols):
            for j in range(lines):
                if j < lines - 1:
                    overlap += min(grid[j][i], grid[j + 1][i])

        return count * 6 - overlap * 2
