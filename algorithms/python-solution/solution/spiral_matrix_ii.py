"""59. Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/


Given a positive integer n, generate a square matrix filled with elements from
1 to n^2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
from typing import List


class Solution:
    def generate_matrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        num = 1
        i, j, direction = 0, 0, 0
        while num <= n * n:
            matrix[i][j] = num
            num += 1
            if direction == 0 and (j < n - 1 and matrix[i][j + 1] == 0) or \
                    direction == 3 and (matrix[i - 1][j] != 0):
                # process right
                direction = 0
                j += 1
            elif direction == 1 and (i < n - 1 and matrix[i + 1][j] == 0) or \
                    direction == 0 and (j == n - 1 or matrix[i][j + 1] != 0):
                # process down
                direction = 1
                i += 1
            elif direction == 2 and (j > 0 and matrix[i][j - 1] == 0) or \
                    direction == 1 and (j == n - 1 or matrix[i][j + 1] != 0):
                # process left
                direction = 2
                j -= 1
            elif direction == 3 and (i > 0 and matrix[i - 1][j] == 0) or \
                    direction == 2 and (j == n - 1 or matrix[i][j + 1] != 0):
                # process up
                direction = 3
                i -= 1
        return matrix
