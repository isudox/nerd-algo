"""
https://leetcode.cn/problems/movement-of-robots/
"""
from typing import List


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        nums = [nums[i] + d * (-1 if c == 'L' else 1) for i, c in enumerate(s)]
        nums.sort()
        base, n = int(1e9 + 7), len(nums)
        return sum([(nums[i] - nums[i - 1]) * i * (n - i) for i in range(1, n)]) % base


if __name__ == '__main__':
    sol = Solution()
    print(sol.sumDistance(nums=[-2, 0, 2], s="RLL", d=3))
