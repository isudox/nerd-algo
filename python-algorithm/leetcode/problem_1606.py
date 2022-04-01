"""1606. Find Servers That Handled Most Number of Requests
https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
"""
import heapq
from typing import List
from sortedcontainers import SortedList


class Solution:
    def busiest_servers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))
        busy = []
        requests = [0] * k
        for i, start in enumerate(arrival):
            while busy and busy[0][0] <= start:
                available.add(busy[0][1])
                heapq.heappop(busy)
            if not available:
                continue
            j = available.bisect_left(i % k)
            if j == len(available):
                j = 0
            idx = available[j]
            requests[idx] += 1
            heapq.heappush(busy, (start + load[i], idx))
            available.remove(idx)
        max_cnt = max(requests)
        ans = []
        for i, req in enumerate(requests):
            if req == max_cnt:
                ans.append(i)
        return ans
