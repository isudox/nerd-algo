"""191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        def low_bit(x: int) -> int:
            return x & -x

        ans = 0
        while n != 0:
            n -= low_bit(n)
            ans += 1
        return ans
