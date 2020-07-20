"""57. Insert Interval
https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their
start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]


Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
from typing import List


class Solution:
    def insert_1(self, intervals, new_interval):
        pass

    def insert_2(self, intervals, new_interval):
        """
        :type intervals: List[List[int]]
        :type new_interval: List[int]
        :rtype: List[List[int]]
        """

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
