"""457. Circular Array Loop
https://leetcode.com/problems/circular-array-loop/
"""
from typing import List


class Solution:
    def circular_array_loop(self, nums: List[int]) -> bool:
        def helper(start: int, cur: int, count: int, visited) -> int:
            if nums[cur] * nums[start] < 0:
                return False
            if cur == start and count > 0:
                return count > 1
            if cur in visited:
                return False
            visited.add(cur)
            next_pos = cur + nums[cur]
            count += 1
            if 0 <= next_pos < len(nums):
                return helper(start, next_pos, count, visited)
            return helper(start, next_pos % len(nums), count, visited)

        for i in range(len(nums)):
            if helper(i, i, 0, set()):
                return True
        return False
