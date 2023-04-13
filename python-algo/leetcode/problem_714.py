"""714. Best Time to Buy and Sell Stock with Transaction Fee
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

Example 1:

Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Note:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""
from typing import List


class Solution:
    def max_profit(self, prices: List[int], fee: int) -> int:
        ans = [0, -prices[0]]
        for i in range(1, len(prices)):
            ans = [max(ans[0], ans[1] + prices[i] - fee),
                   max(ans[0] - prices[i], ans[1])]
        return ans[0]
