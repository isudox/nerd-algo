"""858. Mirror Reflection
https://leetcode.com/problems/mirror-reflection/
"""


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def gcd(a: int, b: int) -> int:
            if a < b:
                return gcd(b, a)
            if b == 0:
                return a
            return gcd(b, a % b)

        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        r = lcm(p, q)
        m, n = r // p, r // q
        if m % 2 == 0 and n % 2 == 1:
            return 0
        if m % 2 == 1 and n % 2 == 1:
            return 1
        if m % 2 == 1 and n % 2 == 0:
            return 2
        return -1
