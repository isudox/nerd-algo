"""764. Largest Plus Sign
https://leetcode.com/problems/largest-plus-sign/
"""
from typing import List


class Solution:
    def order_of_largest_plus_sign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[n] * n for _ in range(n)]
        zeros = set()
        for x, y in mines:
            zeros.add((x, y))
        for i in range(n):
            cnt = 0
            for j in range(n):
                cnt = 0 if (i, j) in zeros else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
            cnt = 0
            for j in range(n - 1, -1, -1):
                cnt = 0 if (i, j) in zeros else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
        for j in range(n):
            cnt = 0
            for i in range(n):
                cnt = 0 if (i, j) in zeros else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
            cnt = 0
            for i in range(n - 1, -1, -1):
                cnt = 0 if (i, j) in zeros else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
        return max(map(max, dp))
