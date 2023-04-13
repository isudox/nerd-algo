"""137. Single Number II
https://leetcode.com/problems/single-number-ii/

Given an integer array nums where every element appears three times except
for one, which appears exactly once. Find the single element and return it.

Example 1:
Input: nums = [2,2,3,2]
Output: 3
Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99

Constraints:

1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each element in nums appears exactly three times except for one element which
appears once.

Follow up: Your algorithm should have a linear runtime complexity. Could you
implement it without using extra memory?
"""
from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2
