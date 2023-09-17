"""1631. Path With Minimum Effort
https://leetcode.com/problems/path-with-minimum-effort/
"""
import sys
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def dfs(x: int, y: int, d: int):
            visited[x][y] = True
            if x == m - 1 and y == n - 1:
                return
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] \
                    and abs(heights[nx][ny] - heights[x][y]) <= d:
                    dfs(nx, ny, d)

        m, n = len(heights), len(heights[0])
        mi = ma = heights[0][0]
        for row in heights:
            for v in row:
                mi = min(mi, v)
                ma = max(ma, v)
        lo, hi = 0, ma - mi
        while lo < hi:
            visited = [[False] * n for _ in range(m)]
            mid = (lo + hi) // 2
            dfs(0, 0, mid)
            if visited[-1][-1]:
                hi = mid
            else:
                lo = mid + 1
        return lo
