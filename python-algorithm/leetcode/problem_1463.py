"""1463. Cherry Pickup II
https://leetcode.com/problems/cherry-pickup-ii/
"""
import functools
from typing import List


def cherry_pickup(grid: List[List[int]]) -> int:
    @functools.lru_cache(None)
    def dfs(x: int, y0: int, y1: int) -> int:
        cur = grid[x][y0] + grid[x][y1] if y0 != y1 else grid[x][y0]
        if x == rows - 1:
            return cur
        nx = x + 1
        ret = 0
        for d0 in [-1, 0, 1]:
            ny0 = y0 + d0
            if ny0 < 0 or ny0 == cols:
                continue
            for d1 in [-1, 0, 1]:
                ny1 = y1 + d1
                if 0 <= ny1 < cols:
                    ret = max(ret, dfs(nx, ny0, ny1))
        return cur + ret

    rows, cols = len(grid), len(grid[0])
    return dfs(0, 0, cols - 1)
