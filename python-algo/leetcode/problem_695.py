"""695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/

You are given an m x n binary matrix grid. An island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You
may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return
0.

Example 1:

Input: grid =
[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected
4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
from typing import List


class Solution:
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            ret = 0
            if visited[x][y]:
                return 0
            visited[x][y] = True
            if grid[x][y] == 1:
                ret = 1
                for d in dirs:
                    if 0 <= x + d[0] < m and 0 <= y + d[1] < n and not visited[x + d[0]][y + d[1]]:
                        ret += dfs(x + d[0], y + d[1])
            return ret

        ans = 0
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                area = dfs(i, j)
                ans = max(ans, area)
        return ans
