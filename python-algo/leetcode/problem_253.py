"""253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals intervals where
intervals[i] = [start_i, end_i], return the minimum number
of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:

1 <= intervals.length <= 10^4
0 <= starti < endi <= 10^6
"""
from typing import List


class Solution:
    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0]))
        cnt = 0
        used = [0] * len(intervals)
        for i in range(len(intervals)):
            if not used[i]:
                cur_end = intervals[i][1]
                for j in range(i + 1, len(intervals)):
                    if not used[j] and cur_end <= intervals[j][0]:
                        cnt += 1
                        cur_end = intervals[j][1]
                        used[j] = 1
        return len(intervals) - cnt
