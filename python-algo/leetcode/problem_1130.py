"""1130. Minimum Cost Tree From Leaf Values
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
"""
from typing import List


class Solution:
    def mct_from_leaf_values(self, arr: List[int]) -> int:
        n = len(arr)
        # dp[i][j]: min sum of non-leaf nodes from subtree formed with arr[i] to arr[j]
        dp = [[2147483647] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        # max[i][j]: the max value of subtree leaf nodes formed with arr[i] to arr[j]
        max_nums = [[0] * n for _ in range(n)]
        for r in range(n):
            for l in range(r, -1, -1):
                if l == r:
                    max_nums[l][r] = arr[r]
                else:
                    max_nums[l][r] = max(max_nums[l + 1][r], arr[l])
        for r in range(n):
            for l in range(r, -1, -1):
                for k in range(l, r):
                    val = max_nums[l][k] * max_nums[k + 1][r]
                    dp[l][r] = min(dp[l][r], val + dp[l][k] + dp[k + 1][r])
        return dp[0][-1]
