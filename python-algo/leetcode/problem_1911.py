"""1911. Maximum Alternating Subsequence Sum
https://leetcode.com/problems/maximum-alternating-subsequence-sum/
"""
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ans = cur = 0
        i = 0
        while i < n:
            while i < n - 1 and nums[i] <= nums[i + 1]:
                i += 1
            cur += nums[i]
            ans = max(ans, cur)
            j = i
            while j < n - 1 and nums[j] >= nums[j + 1]:
                j += 1
            cur -= nums[j]
            i = j + 1
        return ans
