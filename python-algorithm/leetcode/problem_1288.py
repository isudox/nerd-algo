"""1288. Remove Covered Intervals
https://leetcode.com/problems/remove-covered-intervals/
"""
from typing import List


def remove_covered_intervals(intervals: List[List[int]]) -> int:
    n = len(intervals)
    intervals.sort(key=lambda x: (x[0], -x[1]))
    ans = n
    r_max = intervals[0][1]
    for i in range(1, n):
        if intervals[i][1] <= r_max:
            ans -= 1
        else:
            r_max = intervals[i][1]
    return ans
