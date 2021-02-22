"""73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/description/


Given an m x n matrix. If an element is 0, set its entire row and column to
0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best
solution.
Could you devise a constant space solution?

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1
"""
from typing import List


class Solution:
    def set_zeroes(self, matrix: List[List[int]]) -> None:
        def helper(x: int, y: int):
            for i in range(m):
                if i <= x:
                    matrix[i][y] = 0
                elif matrix[i][y] != 0:
                    matrix[i][y] = None
            for i in range(n):
                if i <= y:
                    matrix[x][i] = 0
                elif matrix[x][i] != 0:
                    matrix[x][i] = None

        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    helper(i, j)
                elif matrix[i][j] is None:
                    matrix[i][j] = 0

    def set_zeroes_2(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        memo_rows, memo_cols = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    memo_rows.add(i)
                    memo_cols.add(j)
        for i in range(m):
            for j in range(n):
                if i in memo_rows or j in memo_cols:
                    matrix[i][j] = 0
