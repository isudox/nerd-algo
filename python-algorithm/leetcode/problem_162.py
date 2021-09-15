"""162. Find Peak Element
https://leetcode.com/problems/find-peak-element/
"""
from typing import List


class Solution:
    def find_peak_element(self, nums: List[int]) -> int:
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))
        i, j, ans = 0, len(nums) - 1, -1
        while i < j:
            mid = (i + j) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                i = mid + 1
            else:
                j = mid
        return ans - 1
