"""448. Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
from typing import List


class Solution:
    def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
        """
        nerdy
        """
        n = len(nums)
        store = [False] * (n + 1)
        for num in nums:
            store[num] = True
        ans = []
        for i in range(1, n + 1):
            if not store[i]:
                ans.append(i)
        return []

    def find_disappeared_numbers_2(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans
