"""1219. Path with Maximum Gold
https://leetcode.com/problems/path-with-maximum-gold/
"""
from typing import List


def get_maximum_gold(grid: List[List[int]]) -> int:
    def dfs(x: int, y: int) -> int:
        ret = grid[x][y]
        grid[x][y] = 0
        tmp = 0
        for nx, ny in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                tmp = max(dfs(nx, ny), tmp)
        grid[x][y] = ret
        return ret + tmp

    ans = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0:
                ans = max(ans, dfs(i, j))
    return ans
