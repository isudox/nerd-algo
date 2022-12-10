"""1691. Maximum Height by Stacking Cuboids
https://leetcode.com/problems/maximum-height-by-stacking-cuboids/
"""
from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.sort()
        dp = [0] * len(cuboids)
        for i, (w1, l1, h1) in enumerate(cuboids):
            for j, (w2, l2, h2) in enumerate(cuboids[:i]):
                if l1 >= l2 and h1 >= h2:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += h1
        return max(dp)
