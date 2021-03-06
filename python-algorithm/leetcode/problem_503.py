"""503. Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/

Given a circular array (the next element of the last element is the first
element of the array), print the Next Greater Number for every element. The
Next Greater Number of a number x is the first greater number to its
traversing-order next in the array, which means you could search circularly
to find its next greater number. If it doesn't exist, output -1 for this
number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; The number 2 can't find
next greater number; The second 1's next greater number needs to search
circularly, which is also 2.

Note:
The length of given array won't exceed 10000.
"""
from typing import List


class Solution:
    def next_greater_elements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        size = 2 * n
        for i in range(size):
            i = i % len(nums)
            if stack:
                while stack and nums[stack[-1]] < nums[i]:
                    ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans
