"""502. IPO
https://leetcode.com/problems/ipo/
"""
import heapq
from typing import List


class Solution:
    def find_maximized_capital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = [(capital[i], profits[i]) for i in range(len(capital))]
        pairs.sort(key=lambda x: (x[0]))
        pq = []
        pos = 0
        while k > 0:
            while pos < len(profits) and pairs[pos][0] <= w:
                heapq.heappush(pq, -pairs[pos][1])
                pos += 1
            if pq:
                w += -heapq.heappop(pq)
                k -= 1
            else:
                break
        return w
