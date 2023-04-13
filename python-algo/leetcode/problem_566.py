"""566. Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/
"""
from typing import List


class Solution:
    def matrix_reshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        ans = [[0] * c for _ in range(r)]
        for i in range(m):
            index = n * i
            for j in range(n):
                index += j
                x, y = divmod(index, c)
                ans[x][y] = nums[i][j]
        return ans
