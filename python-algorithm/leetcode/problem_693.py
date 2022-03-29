"""693. Binary Number with Alternating Bits
https://leetcode.com/problems/binary-number-with-alternating-bits/
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre = -1
        while n:
            bit = n & 1
            if pre != -1 and bit ^ pre == 0:
                return False
            pre = bit
            n = n >> 1
        return True
