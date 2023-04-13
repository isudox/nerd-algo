"""322. Coin Change
https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Example 4:

Input: coins = [1], amount = 1
Output: 1

Example 5:

Input: coins = [1], amount = 2
Output: 2
Constraints:

    1 <= coins.length <= 12
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 10^4
"""
from typing import List


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        coins.sort()
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
                continue
            cur = amount
            flag = False
            for coin in coins:
                if i - coin > 0:
                    if dp[i - coin] > 0:
                        flag = True
                        cur = min(cur, dp[i - coin] + 1)
                else:
                    break
            if flag:
                dp[i] = cur
        return dp[amount]
