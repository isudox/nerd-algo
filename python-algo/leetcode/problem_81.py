"""81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def helper(x: int, y: int) -> bool:
            while x <= y:
                mid = x + (y - x) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    x = mid + 1
                else:
                    y = mid - 1
            return False

        pivot = 0
        for i in range(0, len(nums) - 1):
            if nums[i] == target:
                return True
            if nums[i + 1] < nums[i]:
                pivot = i
                break
        if nums[0] <= target <= nums[pivot]:
            return helper(0, pivot)
        return helper(pivot + 1, len(nums) - 1)

    def search2(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            l, m, r = nums[lo], nums[mid], nums[hi]
            if m == target:
                return True
            if l == r == m:
                lo += 1
                hi -= 1
            elif l <= m:
                if l <= target < m:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if m < target <= r:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
