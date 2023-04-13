"""188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

You are given an integer array prices where prices[i] is the price of
a given stock on the ith day.

Design an algorithm to find the maximum profit.
You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6),
profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:

0 <= k <= 10^9
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
import sys
from typing import List


class Solution:
    def max_profit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        if k > n // 2:
            return self.max_profit(n // 2, prices)
        # dp[0][i][j] means holding one stock, the max profit with i-th trx and j-th day.
        dp = [[[0] * (k + 1) for _ in range(n)], [[0] * (k + 1) for _ in range(n)]]
        dp[0][0][0], dp[1][0][0] = -prices[0], 0
        for i in range(1, k + 1):
            dp[0][0][i] = dp[1][0][i] = -sys.maxsize
        for i in range(1, n):
            dp[0][i][0] = max(dp[0][i - 1][0], dp[1][i - 1][0] - prices[i])
            for j in range(1, k + 1):
                dp[0][i][j] = max(dp[0][i - 1][j], dp[1][i - 1][j] - prices[i])
                dp[1][i][j] = max(dp[1][i - 1][j], dp[0][i - 1][j - 1] + prices[i])
        return max(dp[1][n - 1])
