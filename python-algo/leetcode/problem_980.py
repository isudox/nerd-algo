"""980. Unique Paths III
https://leetcode.com/problems/unique-paths-iii/
"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def backtrack(x: int, y: int, zero: int):
            if grid[x][y] == 2:
                if zero == zeros:
                    nonlocal ans
                    ans += 1
                return
            visited[x][y] = True
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != -1:
                    backtrack(nx, ny, zero + (1 if grid[nx][ny] == 0 else 0))
            visited[x][y] = False

        ans = 0
        a, b, zeros = 0, 0, 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zeros += 1
                if grid[i][j] == 1:
                    a, b = i, j
        visited = [[False] * n for _ in range(m)]
        backtrack(a, b, 0)
        return ans
