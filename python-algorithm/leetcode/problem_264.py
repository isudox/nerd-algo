"""264. Ugly Number II
https://leetcode.com/problems/ugly-number-ii/

Given an integer n, return the n^th ugly number.

Ugly number is a positive number whose prime factors only include 2, 3,
and/or 5.

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10
ugly numbers.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 is typically treated as an ugly number.

Constraints:
1 <= n <= 1690
"""


class Solution:
    def nth_ugly_number(self, n: int) -> int:
        dp = [1] * n
        p2 = p3 = p5 = 0
        for i in range(1, n):
            x2 = dp[p2] * 2
            x3 = dp[p3] * 3
            x5 = dp[p5] * 5
            dp[i] = min(x2, x3, x5)
            if x2 == dp[i]:
                p2 += 1
            if x3 == dp[i]:
                p3 += 1
            if x5 == dp[i]:
                p5 += 1
        return dp[-1]
