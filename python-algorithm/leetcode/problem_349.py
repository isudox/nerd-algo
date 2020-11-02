"""349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:

    Each element in the result must be unique.
    The result can be in any order.
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        if (len(nums1) > len(nums2)):
            return self.intersection(nums2, nums1)
        map = {}
        for num in nums1:
            map[num] = True
        ans = []
        for num in nums2:
            if not map:
                return ans
            if num in map:
                ans.append(num)
                del map[num]
        return ans
