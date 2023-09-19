"""2560. House Robber IV
https://leetcode.com/problems/house-robber-iv
"""
from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def helper(mx: int) -> int:
            cnt = i = 0
            while i < len(nums):
                if nums[i] > mx:
                    i += 1
                else:
                    cnt += 1
                    if cnt >= k:
                        return cnt
                    i += 2
            return cnt

        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if helper(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
