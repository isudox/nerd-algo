"""238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,  return an array output
such that output[i] is equal to the product of all the elements of
nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space
complexity analysis.)
"""
from typing import List


class Solution:

    def product_except_self(self, nums: List[int]) -> List[int]:
        count, zeros, product = len(nums), 0, 1
        ans = [1] * count
        for i in range(count):
            product *= nums[i]
            if nums[i] == 0:
                zeros += 1

        for i in range(count):
            if nums[i] == 0:
                if zeros == 1:
                    # if there's one 0 only, then output[i] won't be 0
                    ans[i] = 1
                    for j in range(count):
                        if nums[j] != 0:
                            ans[i] *= nums[j]
                else:
                    ans[i] = 0
            else:
                ans[i] = product // nums[i]
        return ans
