"""798. Smallest Rotation with Highest Score
https://leetcode.com/problems/smallest-rotation-with-highest-score/
"""
from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        def add(x: int, y: int):
            store[x] += 1
            store[y + 1] -= 1

        store = [0] * 100010
        n = len(nums)
        for i in range(n):
            a = (i - n + 1 + n) % n
            b = (i - nums[i] + n) % n
            if a <= b:
                add(a, b)
            else:
                add(0, b)
                add(a, n - 1)
        for i in range(1, n + 1):
            store[i] += store[i - 1]
        ans = 0
        for i in range(1, n + 1):
            if store[i] > store[ans]:
                ans = i
        return ans
