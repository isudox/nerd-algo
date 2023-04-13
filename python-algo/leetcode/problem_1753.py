"""1753. Maximum Score From Removing Stones
https://leetcode.com/problems/maximum-score-from-removing-stones/
"""
import heapq


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        nums = [-a, -b, -c]
        heapq.heapify(nums)
        ans = 0
        while len(nums) >= 2:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            ans += 1
            if x + 1 < 0:
                heapq.heappush(nums, x + 1)
            if y + 1 < 0:
                heapq.heappush(nums, y + 1)
        return ans
