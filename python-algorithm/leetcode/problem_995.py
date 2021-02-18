"""995. Minimum Number of K Consecutive Bit Flips
https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
"""
from typing import List


class Solution:
    def min_k_bit_flips(self, a: List[int], k: int) -> int:
        n = len(a)
        diff = [0] * (n + 1)
        ans = flips = 0
        for i in range(n):
            flips += diff[i]
            if (a[i] + flips) % 2 == 0:
                if i + k > n:
                    return -1
                ans += 1
                flips += 1
                diff[i + k] -= 1
        return ans
