"""1798. Maximum Number of Consecutive Values You Can Make
https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make
"""
from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        target = 1
        coins.sort()
        for coin in coins:
            if coin > target:
                break
            target += coin
        return target
