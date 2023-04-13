"""861. Score After Flipping Matrix
https://leetcode.com/problems/score-after-flipping-matrix/

We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value
in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted
as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Note:

    1 <= A.length <= 20
    1 <= A[0].length <= 20
    A[i][j] is 0 or 1.
"""
from typing import List


class Solution:
    def matrix_score(self, a: List[List[int]]) -> int:
        rows, cols = len(a), len(a[0])
        for row in range(rows):
            if a[row][0] == 0:
                for i in range(cols):
                    a[row][i] = 1 - a[row][i]
        ans = 2 ** (cols - 1) * rows
        for col in range(1, cols):
            count_one = 0
            for row in range(rows):
                if a[row][col] == 1:
                    count_one += 1
            ans += 2 ** (cols - 1 - col) * max(count_one, rows - count_one)
        return ans
