"""766. Toeplitz Matrix
https://leetcode.com/problems/toeplitz-matrix/description/

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise,
return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the
same elements.

Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:

Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you
can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into
the memory at once?
"""


from typing import List


class Solution:
    def is_toeplitz_matrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = m - 1, 0
        count = 0
        while count < m * n:
            i, j = x, y
            while 0 <= i < m and 0 <= j < n:
                if matrix[i][j] != matrix[x][y]:
                    return False
                count += 1
                i, j = i + 1, j + 1
            if x > 0:
                x, y = x - 1, 0
            else:
                y += 1
        return True
