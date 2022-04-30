"""1631. Path With Minimum Effort
https://leetcode.com/problems/path-with-minimum-effort/
"""
import sys
from typing import List


class Solution:
    def minimum_effort_path(self, heights: List[List[int]]) -> int:
        def dfs(x: int, y: int, diff: int):
            memo[x][y] = True
            if x == rows - 1 and y == cols - 1:
                return
            for move_x, move_y in dirs:
                next_x, next_y = x + move_x, y + move_y
                if 0 <= next_x < rows and 0 <= next_y < cols and not memo[next_x][next_y]:
                    if abs(heights[next_x][next_y] - heights[x][y]) <= diff:
                        dfs(next_x, next_y, diff)

        rows, cols = len(heights), len(heights[0])
        minimum, maximum = sys.maxsize, 0
        for i in range(rows):
            for j in range(cols):
                if heights[i][j] < minimum:
                    minimum = heights[i][j]
                if heights[i][j] > maximum:
                    maximum = heights[i][j]
        max_diff, min_diff = maximum - minimum, 0
        memo = [[False] * cols for _ in range(rows)]
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while min_diff < max_diff:
            memo = [[False] * cols for _ in range(rows)]
            mid_diff = (min_diff + max_diff) // 2
            dfs(0, 0, mid_diff)
            if memo[-1][-1]:
                max_diff = mid_diff
            else:
                min_diff = mid_diff + 1
        return min_diff
