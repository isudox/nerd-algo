"""912. Sort an Array
https://leetcode.com/problems/sort-an-array/
"""
from typing import List


class Solution:

    def sort_array(self, nums: List[int]) -> List[int]:
        count = {}
        mi, ma = min(nums), max(nums)
        for num in nums:
            count[num] = count.get(num, 0) + 1
        i = 0
        for num in range(mi, ma + 1):
            while count.get(num, 0):
                nums[i] = num
                i += 1
                count[num] -= 1
        return nums
