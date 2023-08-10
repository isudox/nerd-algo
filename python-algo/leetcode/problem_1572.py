"""1572. Matrix Diagonal Sum
https://leetcode.com/problems/matrix-diagonal-sum/
"""
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n - i - 1]
        return ans if n % 2 == 0 else ans - mat[n // 2][n // 2]
