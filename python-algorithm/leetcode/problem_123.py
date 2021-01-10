"""123. Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""
from typing import List


class Solution:
    def max_p rofit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0
        dp = [[[None, None] for _ in range(3)]] * days
        dp[0][0] = [-prices[0], 0]
        for i in range(1, days):
            dp[i][0] = dp[i - 1][0]
        return dp[-1]
