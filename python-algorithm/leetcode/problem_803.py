"""803. Bricks Falling When Hit
https://leetcode.com/problems/bricks-falling-when-hit/
"""
from typing import List


class Solution:
    def hit_bricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def union(x: int, y: int):
            fx, fy = find(x), find(y)
            if rank[fx] < rank[fy]:
                fx, fy = fy, fx
            uf[fy] = fx
            rank[fx] += rank[fy]
            connected[fy] += connected[fx]

        def find(x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def get_connected(x: int) -> int:
            return connected[find(x)]

        def get_pos(x: int, y: int) -> int:
            return n * x + y

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(grid), len(grid[0])
        size = m * n
        uf, rank, connected = list(range(size + 1)), [1] * (size + 1), [1] * (size + 1)
        for i in range(n):
            if grid[0][i] == 1:
                union(i, size)
        new_grid = [row[:] for row in grid]
        for i, j in hits:
            new_grid[i][j] = 0
        for i in range(1, m):
            for j in range(n):
                if new_grid[i][j] == 1:
                    if new_grid[i - 1][j] == 1:
                        union(get_pos(i - 1, j), get_pos(i, j))
                    if j > 0 and new_grid[i][j - 1] == 1:
                        union(get_pos(i, j - 1), get_pos(i, j))
        ans = []
        for i, j in reversed(hits):
            if new_grid[i][j] == -1:
                ans.append(0)
            else:
                pre_connected = get_connected(size)
                if i == 0:
                    union(j, size)
                for ni, nj in dirs:
                    next_i, next_j = i + ni, j + nj
                    if 0 <= next_i < m and 0 <= next_j < n and new_grid[next_i][next_j]:
                        union(get_pos(i, j), get_pos(next_i, next_j))
                cur_connected = get_connected(size)
                ans.append(max(0, cur_connected - pre_connected - 1))
                new_grid[i][j] = 1
        return ans[::-1]
