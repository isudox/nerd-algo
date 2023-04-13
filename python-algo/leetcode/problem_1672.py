"""1672. Richest Customer Wealth
https://leetcode.com/problems/richest-customer-wealth/
"""
from typing import List


class Solution:
    def maximum_wealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for row in accounts:
            ans = max(ans, sum(row))
        return ans
