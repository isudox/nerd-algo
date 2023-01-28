"""352. Data Stream as Disjoint Intervals
https://leetcode.com/problems/data-stream-as-disjoint-intervals/
"""
import bisect
from typing import List


class SummaryRanges:

    def __init__(self):
        self.intervals = []  # [[1,3], [5,5], [7,9]]
        self.order = []  # [3, 5, 9]

    def addNum(self, value: int) -> None:
        if not self.intervals:
            self.intervals.append([value, value])
            self.order.append(value)
            return
        pos = bisect.bisect_right(self.order, value)  # 向右插入的位置
        self.intervals.insert(pos, [value, value])
        self.order.insert(pos, value)
        deleted = set()
        if pos > 0:
            if self.intervals[pos][0] <= self.intervals[pos - 1][1]:  # [1,3], [3, 3]
                deleted.add(pos)
            elif self.intervals[pos][0] == self.intervals[pos - 1][1] + 1:  # [1,3], [4, 4]
                self.intervals[pos][0] = self.intervals[pos - 1][0]
                self.intervals[pos - 1] = self.intervals[pos]
                deleted.add(pos)
        if pos < len(self.intervals) - 1:
            if self.intervals[pos][1] + 1 == self.intervals[pos + 1][0]:
                self.intervals[pos][1] = self.intervals[pos + 1][1]
                self.intervals[pos + 1] = self.intervals[pos]
                deleted.add(pos + 1)
        new_intervals = []
        new_order = []
        for i, interval in enumerate(self.intervals):
            if i not in deleted:
                new_intervals.append(interval)
                new_order.append(self.order[i])
        self.intervals = new_intervals
        self.order = new_order

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
