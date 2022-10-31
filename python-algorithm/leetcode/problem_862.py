"""862. Shortest Subarray with Sum at Least K
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
"""
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        nums.insert(0, 0)
        ans = len(nums)
        q = []
        for i in range(len(nums)):
            while q and nums[q[-1]] >= nums[i]:
                q.pop()
            while q and nums[i] - nums[q[0]] >= k:
                ans = min(ans, i - q.pop(0))
            q.append(i)
        return -1 if ans == len(nums) else ans
