"""446. Arithmetic Slices II - Subsequence
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
"""
from typing import List


class Solution:
    def number_of_arithmetic_slices(self, nums: List[int]) -> int:
        def dfs(start: int, diff: int, prev: int, cnt: int):
            if start == len(nums) - 1:
                return
            if nums[start + 1] - prev == diff:
                nonlocal ans
                ans += 1
                dfs(start + 1, diff, nums[start + 1], cnt + 1)
            dfs(start + 1, diff, prev, cnt)

        ans = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums)):
                dfs(j, nums[j] - nums[i], nums[j], 2)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.number_of_arithmetic_slices([1, 2, 3, 3]))
    print(sol.number_of_arithmetic_slices([2, 4, 6, 8, 10]))
    print(sol.number_of_arithmetic_slices([7, 7, 7, 7, 7]))
    print(sol.number_of_arithmetic_slices([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
