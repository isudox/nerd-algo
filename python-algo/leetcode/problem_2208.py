"""2208. Minimum Operations to Halve Array Sum
https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
"""
from typing import List
import heapq


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        pq = []
        total = 0
        for num in nums:
            total += num
            heapq.heappush(pq, -num)
        ans, cur = 0, total / 2
        while cur > 0:
            num = heapq.heappop(pq) / 2
            heapq.heappush(pq, num)
            cur += num
            ans += 1
        return ans
