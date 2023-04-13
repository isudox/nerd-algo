"""74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = -1
        x, y = 0, m - 1
        while x <= y:
            mid = x + (y - x) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            if matrix[mid][0] > target:
                y = mid - 1
            else:
                x = mid + 1
        if row == -1:
            return False
        i, j = 0, n - 1
        while i <= j:
            mid = i + (j - i) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False
