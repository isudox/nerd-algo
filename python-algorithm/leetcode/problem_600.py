"""600. Non-negative Integers without Consecutive Ones
https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
"""
import math
from functools import lru_cache


class Solution:
    def find_integers(self, n: int) -> int:
        @lru_cache(None)
        def dfs(pos: int, bits: int) -> int:
            if pos == m:
                return 1
            last_bit = bits & 1
            ret = 0
            bits = bits << 1
            if bits <= n:  # cur pos pick 0
                ret += dfs(pos + 1, bits)
            if last_bit == 0 and bits + 1 <= n:  # cur pos pick 1
                ret += dfs(pos + 1, bits + 1)
            return ret

        dp = [[0, 0] for _ in range(31)]
        dp[1][0] = 1
        dp[1][1] = 2
        for i in range(1, 30):
            dp[i + 1][0] = dp[i][1]
            dp[i + 1][1] = dp[i][0] + dp[i][1]
        ans = 0
        pre = 0
        for i in range(30, -1, -1):
            bit = (n >> i) & 1
            if bit == 1:
                ans += dp[i + 1][0]
                if pre == 1:
                    break
            pre = bit
            if i == 0:
                ans += 1
        return ans
