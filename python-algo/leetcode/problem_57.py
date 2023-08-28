"""57. Insert Interval
https://leetcode.com/problems/insert-interval/
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals
        for i, interval in enumerate(intervals):
            if interval[0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                break
            if i == len(intervals) - 1:
                intervals.append(newInterval)
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][0] = min(ans[-1][0], intervals[i][0])
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans
