"""633. Sum of Square Numbers
https://leetcode.com/problems/sum-of-square-numbers/

Given a non-negative integer c, decide whether there're two integers a and b
such that a^2 + b^2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false

Example 3:

Input: c = 4
Output: true

Example 4:

Input: c = 2
Output: true

Example 5:

Input: c = 1
Output: true

Constraints:

0 <= c <= 2^31 - 1
"""
import math


class Solution:
    def judge_square_sum(self, c: int) -> bool:
        lo, hi = 0, int(math.sqrt(c))
        while lo <= hi:
            cur = lo * lo + hi * hi
            if cur == c:
                return True
            if cur < c:
                lo += 1
            else:
                hi -= 1
        return False
