"""1034. Coloring A Border
https://leetcode.com/problems/coloring-a-border/
"""
import copy
from typing import List


# TODO
class Solution:
    def color_border(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def dfs(x: int, y: int, old_color: int):
            grid[x][y] = color
            modified[x][y] = True
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == old_color and not modified[nx][ny]:
                    dfs(nx, ny, old_color)

        origin_grid = copy.deepcopy(grid)
        m, n = len(grid), len(grid[0])
        old_color = grid[row][col]
        modified = [[False] * n for _ in range(m)]
        dfs(row, col, old_color)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == color:
                    if 0 < i < m - 1 and 0 < j < n - 1:
                        cnt = 0
                        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                            if grid[i + di][j + dj] == color and (modified[i + di][j + dj] or origin_grid[i+di][j+dj] != color):
                                cnt += 1
                        if cnt == 4:
                            grid[i][j] = old_color
        return grid


if __name__ == '__main__':
    sol = Solution()
    print(sol.color_border([[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]],1,3,1))
    print(sol.color_border([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2))
    print(sol.color_border([[1,1],[1,2]],0,0,3))
