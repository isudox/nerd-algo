"""56. Merge Intervals
https://leetcode.com/problems/merge-intervals/


Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def sort_list(lst: List[List[int]]):
            return sorted(lst, key=lambda x: x[0])

        def is_overlap(l1: List[int], l2: List[int]):
            if l1[1] < l2[0] or l1[0] > l2[1]:
                return False
            return True

        def merge_list(l1: List[int], l2: List[int]):
            left = min(l1[0], l1[1], l2[0], l2[1])
            right = max(l1[0], l1[1], l2[0], l2[1])
            l1[0] = left
            l1[1] = right

        if not intervals:
            return intervals
        intervals = sort_list(intervals)
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if is_overlap(ans[-1], intervals[i]):
                merge_list(ans[-1], intervals[i])
            else:
                ans.append(intervals[i])
        return ans
