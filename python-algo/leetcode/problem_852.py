"""852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i, j = 1, len(arr) - 2
        while i < j:
            k = (i + j) // 2
            if arr[k - 1] < arr[k] and arr[k] > arr[k + 1]:
                return k
            if arr[k - 1] < arr[k] < arr[k + 1]:
                i = k + 1
            else:
                j = k - 1
        return i
