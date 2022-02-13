"""1020. Number of Enclaves
https://leetcode.com/problems/number-of-enclaves/
"""
from typing import List


def num_enclaves(grid: List[List[int]]) -> int:
    def dfs(x: int, y: int):
        grid[x][y] = 0
        for nx, ny in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                dfs(nx, ny)

    ans = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                dfs(i, j)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                ans += 1
    return ans
