"""768. Max Chunks To Make Sorted II
https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
"""
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        sorted_arr = sorted(arr)
        for i in range(1, n):
            arr[i] += arr[i - 1]
            sorted_arr[i] += sorted_arr[i - 1]
        ans = 0
        for i in range(n):
            if arr[i] == sorted_arr[i]:
                ans += 1
        return ans
