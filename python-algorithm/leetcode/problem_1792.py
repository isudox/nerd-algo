"""1792. Maximum Average Pass Ratio
https://leetcode.com/problems/maximum-average-pass-ratio/
"""
import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = [Entry(p, t) for p, t in classes]
        heapq.heapify(pq)
        for _ in range(extraStudents):
            heapq.heapreplace(pq, Entry(pq[0].p + 1, pq[0].t + 1))
        return sum(e.p/e.t for e in pq) / len(pq)


class Entry:
    def __init__(self, p: int, t: int):
        self.p = p  # pass
        self.t = t  # total

    def __lt__(self, other: 'Entry') -> bool:
        return (self.t - self.p) * other.t * (other.t + 1) > (other.t - other.p) * self.t * (self.t + 1)
