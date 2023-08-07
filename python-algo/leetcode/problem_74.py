"""74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
"""
from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = [row[0] for row in matrix]
        pos = bisect.bisect_right(col, target)
        if pos == 0:
            return False
        if pos == len(col) and target > matrix[-1][-1]:
            return False
        row = matrix[pos - 1]
        pos = bisect.bisect_left(row, target)
        return pos < len(matrix[0]) and row[pos] == target
