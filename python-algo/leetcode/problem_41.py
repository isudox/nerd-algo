"""41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
from typing import List


class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:
        ans = 1
        checked = {}
        for num in nums:
            if num > 0:
                checked[num] = True
                if num == ans:
                    while checked.get(ans):
                        ans += 1
        return ans
