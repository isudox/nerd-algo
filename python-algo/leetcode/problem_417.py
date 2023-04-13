"""417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/
"""
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(x: int, y: int, visited: List[List[bool]]) -> None:
            if visited[x][y]:
                return
            visited[x][y] = True
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                    dfs(nx, ny, visited)
            
        m, n = len(heights), len(heights[0])
        atlantic = [[False] * n for _ in range(m)]
        pacific = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dfs(i, j, pacific)
                if i == m - 1 or j == n - 1:
                    dfs(i, j, atlantic)
        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans

