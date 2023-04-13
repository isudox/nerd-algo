"""1995. Count Special Quadruplets
https://leetcode.com/problems/count-special-quadruplets/
"""
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 3):
            for j in range(i+1, n-2):
                for k in range(j + 1, n - 1):
                    summary = nums[i] + nums[j] + nums[k]
                    for x in range(k + 1, n):
                        if nums[x] == summary:
                            ans += 1
        return ans
