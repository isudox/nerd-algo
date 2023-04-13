import heapq
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        pq = []
        heapq.heapify(pq)
        for num in amount:
            if num > 0:
                heapq.heappush(pq, -num)
        ans = 0
        while pq:
            if len(pq) == 1:
                ans -= heapq.heappop(pq)
                break
            a, b = heapq.heappop(pq), heapq.heappop(pq),
            ans += 1
            if a + 1 != 0:
                heapq.heappush(pq, a + 1)
            if b + 1 != 0:
                heapq.heappush(pq, b + 1)
        return ans
