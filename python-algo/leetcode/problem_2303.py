"""2303. Calculate Amount Paid in Taxes
https://leetcode.com/problems/calculate-amount-paid-in-taxes/
"""
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0.0
        pre = 0
        for upper, p in brackets:
            if income == 0:
                break
            cur = min(upper - pre, income)
            ans += cur * p / 100
            income -= cur
            pre = upper
        return ans
