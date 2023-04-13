"""313. Super Ugly Number
https://leetcode.com/problems/super-ugly-number/
"""
import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        store = []
        heapq.heapify(store)
        heapq.heappush(store, 1)
        visited = {1}
        while n > 1:
            num = heapq.heappop(store)
            n -= 1
            for prime in primes:
                new_num = num * prime
                if new_num not in visited:
                    visited.add(new_num)
                    heapq.heappush(store, new_num)
        return store[0]
