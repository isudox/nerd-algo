"""2500. Delete Greatest Value in Each Row
https://leetcode.com/problems/delete-greatest-value-in-each-row/
"""
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)
        ans = 0
        for i in range(len(grid[0])):
            cur = grid[0][i]
            for j in range(len(grid)):
                cur = max(cur, grid[j][i])
            ans += cur
        return ans
