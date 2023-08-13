"""518. Coin Change 2
https://leetcode.com/problems/coin-change-2/
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]
        return dp[-1][-1]

    def change2(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]

    def change3(self, amount: int, coins: List[int]) -> int:
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0
            if j == 0:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = dfs(i - 1, j) + (dfs(i, j - coins[i]) if j >= coins[i] else 0)
            return memo[i][j]

        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        return dfs(len(coins) - 1, amount)
