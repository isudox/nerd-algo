"""118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List


class Solution:
    def generate(self, rows: int) -> List[List[int]]:
        ans = []
        row = 1
        while row <= rows:
            cur = [1] * row
            for i in range(1, (row + 1) // 2):
                cur[i] = cur[row - 1 - i] = ans[-1][i - 1] + ans[-1][i]
            ans.append(cur)
            row += 1
        return ans
