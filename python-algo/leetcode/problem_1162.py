"""1162. As Far from Land as Possible
https://leetcode.com/problems/as-far-from-land-as-possible/
"""
import collections
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = -1
        q = collections.deque()
        store = collections.defaultdict(int)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    store[i * n + j] = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            dx, dy = q.popleft()
            step = store.get(dx * n + dy)
            for a, b in dirs:
                nx, ny = dx + a, dy + b
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] != 0:
                        continue
                    grid[nx][ny] = step + 1
                    q.append((nx, ny))
                    store[nx * n + ny] = step + 1
                    ans = max(ans, step + 1)
        return ans
