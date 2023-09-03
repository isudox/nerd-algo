"""2366. Minimum Replacements to Sort the Array
https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
"""
from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            cnt = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
            ans += cnt - 1
            nums[i] = nums[i] // cnt
        return ans
