"""120. Triangle
https://leetcode.com/problems/triangle/

Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
"""
from typing import List


class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[] for _ in range(n)]
        dp[0].append(triangle[0][0])
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    cur = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    cur = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    cur = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
                dp[i].append(cur)
        return min(dp[-1])

    def minimum_total_1(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]
        temp = []
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    temp.append(dp[j] + triangle[i][j])
                elif j == i:
                    temp.append(dp[j - 1] + triangle[i][j])
                else:
                    temp.append(min(dp[j], dp[j - 1]) + triangle[i][j])
            dp = temp
            temp = []
        return min(dp)


