"""1846. Maximum Element After Decreasing and Rearranging
https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
"""
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            if diff <= 1:
                continue
            if diff > 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]