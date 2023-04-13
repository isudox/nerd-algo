"""309. Best Time to Buy and Sell Stock with Cooldown
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like
(ie, buy one and sell one share of the stock multiple times)
with the following restrictions:

You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day.
(ie, cooldown 1 day)

Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        # dp[i][0] = buy, dp[i][1] = sell, dp[i][0] = cooldown
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][2] - prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][0], dp[i - 1][2])
        return dp[-1][1]
