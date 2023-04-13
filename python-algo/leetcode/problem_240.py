"""240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.
Given target = 20, return false.
"""
from typing import List


class Solution:
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(x1: int, y1: int, x2: int, y2: int) -> bool:
            if x1 > x2 or y1 > y2:
                return False
            if target < matrix[x1][y1] or target > matrix[x2][y2]:
                return False
            if target == matrix[x1][y1] or target == matrix[x2][y2]:
                return True
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2
            if matrix[mid_x][mid_y] == target:
                return True
            if matrix[mid_x][mid_y] < target:
                return binary_search(mid_x + 1, y1, x2, y2) or binary_search(x1, mid_y + 1, mid_x, y2)
            else:
                return binary_search(x1, y1, mid_x - 1, y2) or binary_search(mid_x, y1, x2, mid_y - 1)

        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        return binary_search(0, 0, rows - 1, cols - 1)
