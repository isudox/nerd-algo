"""1588. Sum of All Odd Length Subarrays
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
"""
from typing import List


class Solution:
    def sum_odd_length_subarrays(self, arr: List[int]) -> int:
        pre_sums = [0]
        for num in arr:
            pre_sums.append(pre_sums[-1] + num)
        ans = 0
        n = len(arr)
        for i in range(n):
            for j in range(1, n + 1 - i, 2):
                ans += pre_sums[i + j] - pre_sums[i]
        return ans
