"""502. IPO
https://leetcode.com/problems/ipo/
"""
import heapq
from typing import List


class Solution:
    def find_maximized_capital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = list(zip(capital, profits))
        pairs.sort(key=lambda x: x[0])
        pq = []
        i = 0
        while k:
            while i < len(profits) and pairs[i][0] <= w:
                heapq.heappush(pq, -pairs[i][1])
                i += 1
            if not pq:
                break
            w -= heapq.heappop(pq)
            k -= 1
        return w
