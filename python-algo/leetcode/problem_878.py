"""878. Nth Magical Number
https://leetcode.com/problems/nth-magical-number/
"""
import math


class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        base = int(1e9 + 7)
        lcm = a // math.gcd(a, b) * b

        def magic_below_x(x):
            return x // a + x // b - x // lcm

        lo = 0
        hi = n * min(a, b)
        while lo < hi:
            mi = (lo + hi) // 2
            if magic_below_x(mi) < n:
                lo = mi + 1
            else:
                hi = mi

        return lo % base
