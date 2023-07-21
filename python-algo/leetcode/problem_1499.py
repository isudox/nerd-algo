"""1499. Max Value of Equation
https://leetcode.cn/problems/max-value-of-equation/
"""
from typing import List
import heapq


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = -float('inf')
        pq = []
        for x, y in points:
            while pq and x - pq[0][1] > k:
                heapq.heappop(pq)
            if pq:
                ans = max(ans, x + y - pq[0][0])
            heapq.heappush(pq, (x - y, x))
        return ans
