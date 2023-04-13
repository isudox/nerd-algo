"""871. Minimum Number of Refueling Stops
https://leetcode.com/problems/minimum-number-of-refueling-stops/
"""
import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        ans = 0
        fuel = startFuel
        for i in range(len(stations) + 1):
            nxt = stations[i][0] if i < len(stations) else target
            cur = 0 if i == 0 else stations[i - 1][0]
            fuel -= nxt - cur
            while fuel < 0 and pq:
                fuel += -heapq.heappop(pq)
                ans += 1
            if fuel < 0:
                return -1
            if i < len(stations):
                heapq.heappush(pq, -stations[i][1])
        return ans
