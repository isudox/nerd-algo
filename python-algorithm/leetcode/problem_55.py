"""55. Jump Game
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump
             length is 0, which makes it impossible to reach the last index.
"""
from typing import List


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        def indexes_of(lst, item):
            return [i for i, x in enumerate(lst) if x == item]

        if 0 not in nums:
            return True
        # sufficient and necessary condition to fail: always jump to 0.
        length = len(nums)
        zero_indexes = indexes_of(nums, 0)
        for index in zero_indexes:
            skip_zero = False
            for i in range(index + 1):
                if nums[i] <= index - i:
                    if nums[i] + i >= length - 1:
                        return True
                # if nums[i] > zero_index - i, means it can jump over 0.
                else:
                    skip_zero = True
                    break
            if not skip_zero:
                return False
        return True
