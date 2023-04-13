"""1590. Make Sum Divisible by P
https://leetcode.com/problems/make-sum-divisible-by-p/
"""
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        summ = sum(nums)
        rem = summ % p
        if rem == 0:
            return 0
        pre_sum = []
        for i, num in enumerate(nums):
            pre_sum.append(num % p if i == 0 else (pre_sum[-1] + num) % p)
        last_seen = {0: -1}
        ans = len(nums)
        for i, cur in enumerate(pre_sum):
            need = (cur + p - rem) % p
            if need in last_seen:
                ans = min(ans, i - last_seen[need])
            last_seen[cur] = i
        return -1 if ans >= len(nums) else ans
