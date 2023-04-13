"""329. Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary
(i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6].
Moving diagonally is not allowed.
"""
from typing import List


class Solution:
    def longest_increasing_path(self, matrix: List[List[int]]) -> int:
        def find_path(x: int, y: int) -> int:
            if memo[x][y] != 0:
                return memo[x][y]
            ans = 1
            if x + 1 < rows and matrix[x + 1][y] > matrix[x][y]:
                ans = max(ans, 1 + find_path(x + 1, y))
            if x - 1 >= 0 and matrix[x - 1][y] > matrix[x][y]:
                ans = max(ans, 1 + find_path(x - 1, y))
            if y - 1 >= 0 and matrix[x][y - 1] > matrix[x][y]:
                ans = max(ans, 1 + find_path(x, y - 1))
            if y + 1 < cols and matrix[x][y + 1] > matrix[x][y]:
                ans = max(ans, 1 + find_path(x, y + 1))
            memo[x][y] = ans
            return ans

        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        max_path = 0
        for i in range(rows):
            for j in range(cols):
                max_path = max(max_path, find_path(i, j))
        return max_path
