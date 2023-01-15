"""2293. Min Max Game
https://leetcode.com/problems/min-max-game/
"""
from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            tmp = [0] * (len(nums) // 2)
            for i in range(len(tmp)):
                if i % 2 == 0:
                    tmp[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    tmp[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = tmp
        return nums[0]
