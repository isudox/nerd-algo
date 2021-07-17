"""1846. Maximum Element After Decreasing and Rearranging
https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
"""
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]

    def maximumElementAfterDecrementingAndRearranging2(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = [0] * (n + 1)
        for num in arr:
            if num <= n:
                cnt[num] += 1
            else:
                cnt[n] += 1
        miss = 0
        for i in range(1, n + 1):
            if cnt[i] == 0:
                miss += 1
            else:
                miss -= min(cnt[i] - 1, miss)
        return n - miss