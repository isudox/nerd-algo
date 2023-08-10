"""2616. Minimize the Maximum Difference of Pairs
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
"""
from typing import List
from bisect import bisect_left


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def helper(x: int) -> int:
            cnt = i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= x:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), p, key=helper)
