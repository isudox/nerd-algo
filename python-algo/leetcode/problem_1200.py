"""1200. Minimum Absolute Difference
https://leetcode.com/problems/minimum-absolute-difference/
"""
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = arr[1] - arr[0]
        ans = [[arr[0], arr[1]]]
        for i in range(2, len(arr)):
            cur_diff = arr[i] - arr[i - 1]
            if cur_diff == min_diff:
                ans.append([arr[i - 1], arr[i]])
            elif cur_diff < min_diff:
                min_diff = cur_diff
                ans = [[arr[i - 1], arr[i]]]
        return ans
