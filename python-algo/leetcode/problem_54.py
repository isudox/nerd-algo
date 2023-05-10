"""54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/
"""
from typing import List


class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ans = []
        row, col = len(matrix), len(matrix[0])
        i, j, count, direction = 0, 0, 0, 0
        while count < row * col:
            ans.append(matrix[i][j])
            matrix[i][j] = None
            count += 1
            if direction == 0 and (j < col - 1 and matrix[i][j + 1] is not None) \
                    or direction == 3 and (matrix[i - 1][j] is None):
                # process right
                direction = 0
                j += 1
            elif direction == 1 and (
                    i < row - 1 and matrix[i + 1][j] is not None) or \
                    direction == 0 and (
                    j == col - 1 or matrix[i][j + 1] is None):
                # process down
                direction = 1
                i += 1
            elif direction == 2 and (j > 0 and matrix[i][j - 1] is not None) or \
                    direction == 1 and (
                    j == col - 1 or matrix[i][j + 1] is None):
                # process left
                direction = 2
                j -= 1
            elif direction == 3 and (i > 0 and matrix[i - 1][j] is not None) or \
                    direction == 2 and (
                    j == col - 1 or matrix[i][j + 1] is None):
                # process up
                direction = 3
                i -= 1
        return ans
