"""1137. N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        def helper(x: int) -> int:
            if memo[x] != 0:
                return memo[x]
            if x == 0:
                return 0
            if x == 1 or x == 2:
                return 1
            memo[x] = helper(x - 3) + helper(x - 2) + helper(x - 1)
            return memo[x]

        memo = [0] * (n + 1)
        return helper(n)
