"""1851. Minimum Interval to Include Each Query
https://leetcode.com/problems/minimum-interval-to-include-each-query/
"""
import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        qindex = list(range(len(queries)))
        qindex.sort(key=lambda x: queries[x])
        intervals.sort(key=lambda x: x[0])
        pq = []
        ans = [-1] * len(queries)
        i = 0
        for qi in qindex:
            while i < len(intervals) and intervals[i][0] <= queries[qi]:
                heapq.heappush(pq, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1],))
                i += 1
            while pq and pq[0][2] < queries[qi]:
                heapq.heappop(pq)
            if pq:
                ans[qi] = pq[0][0]
        return ans
