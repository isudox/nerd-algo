"""260. Single Number III
https://leetcode-cn.com/problems/single-number-iii/

Given an integer array nums, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the two elements that
appear only once. You can return the answer in any order.

Follow up: Your algorithm should run in linear runtime complexity. Could you
implement it using only constant space complexity?

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:

Input: nums = [-1,0]
Output: [-1,0]

Example 3:

Input: nums = [0,1]
Output: [1,0]

Constraints:

    2 <= nums.length <= 3 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    Each integer in nums will appear twice, only two integers will appear once.
"""
from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> List[int]:
        ans = []
        memo = dict()
        for num in nums:
            if num in memo:
                del memo[num]
            else:
                memo[num] = 1
        for num in memo.keys():
            ans.append(num)
        return ans
