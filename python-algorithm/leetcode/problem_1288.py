"""1288. Remove Covered Intervals
https://leetcode.com/problems/remove-covered-intervals/
"""
from typing import List


def remove_covered_intervals(intervals: List[List[int]]) -> int:
    n = len(intervals)
    intervals.sort(key=lambda x: (-x[0], x[1]))
    removed = 0
    for i in range(n):
        for j in range(i + 1, n):
            if intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                removed += 1
                break
    return n - removed
