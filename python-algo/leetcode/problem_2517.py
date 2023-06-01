"""2517. Maximum Tastiness of Candy Basket
https://leetcode.com/problems/maximum-tastiness-of-candy-basket/
"""
from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def helper(x: int) -> int:
            pre = price[0]
            cnt = 1
            for p in price:
                if p - pre >= x:
                    cnt += 1
                    pre = p
            return cnt

        price.sort()
        lo, hi = 0, (price[-1] - price[0]) // (k - 1)
        while lo <= hi:
            mid = (lo + hi) >> 1
            if helper(mid) >= k:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
