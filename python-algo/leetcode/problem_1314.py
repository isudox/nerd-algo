"""1314. Matrix Block Sum
https://leetcode.com/problems/matrix-block-sum/

Given a m x n matrix mat and an integer k, return a matrix answer where each
answer[i][j] is the sum of all elements mat[r][c] for:

  i - k <= r <= i + k,
  j - k <= c <= j + k, and
  (r, c) is a valid position in the matrix.

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100
"""
from typing import List


class Solution:
    def matrix_block_sum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        def get(x, y):
            nonlocal pre_sums
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return pre_sums[x][y]

        m, n = len(mat), len(mat[0])
        pre_sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_sums[i][j] = pre_sums[i - 1][j] + pre_sums[i][j - 1] - pre_sums[i - 1][j - 1] + mat[i - 1][j - 1]
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + k + 1, j + k + 1) - get(i - k, j + k + 1) - get(i + k + 1, j - k) + get(i - k, j - k)
        return ans
