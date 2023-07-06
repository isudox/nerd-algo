"""2679. Sum in a Matrix
https://leetcode.cn/problems/sum-in-a-matrix/
"""
from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        ans = 0
        for i in range(len(nums[0])):
            tmp = nums[0][i]
            for row in nums:
                tmp = max(tmp, row[i])
            ans += tmp
        return ans
