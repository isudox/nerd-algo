"""485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
from typing import List


class Solution:
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        i = j = ans = 0
        while j < len(nums):
            if nums[j] == 0:
                if j - i > ans:
                    ans = j - i
                j += 1
                i = j
            else:
                j += 1
        if j - i > ans:
            ans = j - i
        return ans

    def find_max_consecutive_ones_2(self, nums: List[int]) -> int:
        ans = cur = 0
        for num in nums:
            if num == 1:
                cur += 1
            else:
                if cur > ans:
                    ans = cur
                cur = 0
        if cur > ans:
            ans = cur
        return ans
