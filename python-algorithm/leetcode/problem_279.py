"""279. Perfect Squares
https://leetcode.com/problems/perfect-squares/

Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
from typing import List
import math


class Solution:
    def num_squares(self, n: int) -> int:
        def dfs(k: int, memo: List[int]) -> int:
            if k in memo:
                return memo[k]
            start = int(math.sqrt(k))
            ret = k
            while start:
                ret = min(ret, 1 + dfs(k - start ** 2, memo))
                start -= 1
            memo[k] = ret
            return ret

        return dfs(n, [0] * (n + 1))

    def num_squares_2(self, n: int) -> int:
        def init_squares(k: int) -> List[int]:
            squares = []
            prev, i = 0, 0
            while prev < k:
                prev = (i << 1) + 1 + prev
                squares.append(prev)
                i += 1
            return squares

        dp = [0] * (n + 1)
        squares = init_squares(n)
        for i in range(1, n + 1):
            dp[i] = i
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i - square])
        return dp[n]

    def num_squares_3(self, n: int) -> int:
        def can_divide(m: int, k: int) -> bool:
            nonlocal square_nums
            if k == 1:
                return m in square_nums
            for square in square_nums:
                if can_divide(m - square, k - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n ** 0.5) + 1)])
        for i in range(1, n + 1):
            if can_divide(n, i):
                return i
