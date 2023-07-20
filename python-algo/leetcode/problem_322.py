"""322. Coin Change
https://leetcode.com/problems/coin-change/
"""
from typing import List


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i],  dp[i - coin] + 1)
        return dp[-1] if dp[-1] < amount + 1 else -1
