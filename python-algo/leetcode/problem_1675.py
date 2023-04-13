"""1675. Minimize Deviation in Array
https://leetcode.com/problems/minimize-deviation-in-array/
"""
import heapq
from typing import List


class Solution:
    def minimum_deviation(self, nums: List[int]) -> int:
        pq = []
        for num in nums:
            a = num
            while a & 1 == 0:
                a = a >> 1
            heapq.heappush(pq, [a, num])
        ans = float('inf')
        maximum = max(a for a, _ in pq)
        while len(pq) == len(nums):
            a, num = heapq.heappop(pq)
            ans = min(ans, maximum - a)
            if a & 1 == 1 or a < num:
                maximum = max(maximum, a * 2)
                heapq.heappush(pq, [a * 2, num])
        return ans
