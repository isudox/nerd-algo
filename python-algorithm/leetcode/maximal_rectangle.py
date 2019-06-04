"""85. Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/


Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
containing only 1's and return its area.

Example:


Input:
[
⁠ ["1","0","1","0","0"],
⁠ ["1","0","1","1","1"],
⁠ ["1","1","1","1","1"],
⁠ ["1","0","0","1","0"]
]
Output: 6
"""
from typing import List


class Solution:
    def maximal_rectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        for _ in range(cols):
            pass
        for _ in range(rows):
            pass
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[rows - 1][cols - 1]
