"""565. Array Nesting
https://leetcode.com/problems/array-nesting/
"""
from typing import List


class Solution:
    def array_nesting(self, nums: List[int]) -> int:
        ans = 0
        visited = [False] * len(nums)
        for i in range(len(nums)):
            if not visited[i]:
                start, cnt = nums[i], 0
                while True:
                    start = nums[start]
                    cnt += 1
                    visited[start] = True
                    if start == nums[i]:
                        break
                ans = max(ans, cnt)
        return ans
