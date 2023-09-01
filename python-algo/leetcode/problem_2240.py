"""2240. Number of Ways to Buy Pens and Pencils
https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils
"""


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        for i in range(0, total + 1, cost1):
            rem = total - i
            ans += rem // cost2 + 1
        return ans
