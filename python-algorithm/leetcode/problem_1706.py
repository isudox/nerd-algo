"""1706. Where Will the Ball Fall
https://leetcode.com/problems/where-will-the-ball-fall/
"""
from typing import List


def find_ball(grid: List[List[int]]) -> List[int]:
    m, n = len(grid), len(grid[0])
    ans = [0] * n
    for i in range(n):
        row, col = 0, i
        while row < m:
            if grid[row][col] == 1:
                if col == n - 1 or grid[row][col + 1] == -1:
                    ans[i] = -1
                    break
                col += 1
            else:
                if col == 0 or grid[row][col - 1] == 1:
                    ans[i] = -1
                    break
                col -= 1
            row += 1
        if row >= m:
            ans[i] = col
    return ans
