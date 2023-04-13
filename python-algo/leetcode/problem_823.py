"""823. Binary Trees With Factors
https://leetcode.com/problems/binary-trees-with-factors/
"""
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        base = int(1e9 + 7)
        n = len(arr)
        arr.sort()
        store = {num: i for i, num in enumerate(arr)}
        dp = [1] * n
        for i, num in enumerate(arr):
            for j in range(i):
                if num % arr[j] == 0:
                    right = num // arr[j]
                    if right in store:
                        dp[i] = (dp[i] + dp[j] * dp[store[right]]) % base
        return sum(dp) % base
