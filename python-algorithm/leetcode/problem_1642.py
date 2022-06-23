"""1642. Furthest Building You Can Reach
https://leetcode.com/problems/furthest-building-you-can-reach/
"""
from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hq = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(hq, diff)
            if len(hq) > ladders:
                bricks -= heapq.heappop(hq)
            if bricks < 0:
                return i
        return len(heights) - 1
