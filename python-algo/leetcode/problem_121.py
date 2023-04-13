"""121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        ans = 0
        mi = prices[0]
        for p in prices:
            if p < mi:
                mi = p
            else:
                ans = max(ans, p - mi)
        return ans
