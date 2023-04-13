"""1475. Final Prices With a Special Discount in a Shop
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
"""
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    ans.append(prices[i] - prices[j])
                    break
            else:
                ans.append(prices[i])
        return ans
