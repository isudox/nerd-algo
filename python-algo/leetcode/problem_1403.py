"""1403. Minimum Subsequence in Non-Increasing Order
https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
"""
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        summ = sum(nums)
        ans = []
        tmp = 0
        for num in nums:
            ans.append(num)
            tmp += num
            if tmp * 2 > summ:
                return ans
        return ans

