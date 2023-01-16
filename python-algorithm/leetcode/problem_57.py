"""57. Insert Interval
https://leetcode.com/problems/insert-interval/
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        def sort_list(arr: List[List[int]]):
            return sorted(arr, key=lambda x: x[0])

        def is_overlap(arr1: List[int], arr2: List[int]):
            return arr1[1] >= arr2[0] and arr1[0] <= arr2[1]

        def merge_list(arr1: List[int], arr2: List[int]):
            left = min(arr1[0], arr1[1], arr2[0], arr2[1])
            right = max(arr1[0], arr1[1], arr2[0], arr2[1])
            arr1[0], arr1[1] = left, right

        if not new_interval:
            return intervals

        intervals.append(new_interval)
        intervals = sort_list(intervals)
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if is_overlap(ans[-1], intervals[i]):
                merge_list(ans[-1], intervals[i])
            else:
                ans.append(intervals[i])
        return ans
