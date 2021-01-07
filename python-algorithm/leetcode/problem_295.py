"""295. Find Median from Data Stream

Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
import bisect


class MedianFinder:

    def __init__(self):
        self.store = []
        self.size = 0

    def add_num(self, num: int) -> None:
        bisect.insort_left(self.store, num)
        self.size += 1

    def find_median(self) -> float:
        if self.size % 2 == 1:
            return self.store[self.size // 2]
        else:
            return (self.store[self.size // 2] + self.store[self.size // 2 - 1]) / 2
