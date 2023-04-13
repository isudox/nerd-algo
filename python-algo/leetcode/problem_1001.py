"""1001. Grid Illumination
https://leetcode.com/problems/grid-illumination/
"""
import collections
from typing import List


def grid_illumination(n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
    lights = set()
    row, col = collections.Counter(), collections.Counter()
    diag1, diag2 = collections.Counter(), collections.Counter()
    for (i, j) in lamps:
        if (i, j) in lights:
            continue
        lights.add((i, j))
        row[i] += 1
        col[j] += 1
        diag1[j - i] += 1
        diag2[j + i] += 1
    ans = []
    for (x, y) in queries:
        if row[x] or col[y] or diag1[y - x] or diag2[y + x]:
            ans.append(1)
        else:
            ans.append(0)
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) in lights:
                    lights.remove((nx, ny))
                    row[nx] -= 1
                    col[ny] -= 1
                    diag1[ny - nx] -= 1
                    diag2[ny + nx] -= 1
    return ans
