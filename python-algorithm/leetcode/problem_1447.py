"""1447. Simplified Fractions
https://leetcode.com/problems/simplified-fractions/
"""
from typing import List


def simplified_fractions(n: int) -> List[str]:
    def gcd(a: int, b: int) -> int:
        if a < b:
            return gcd(b, a)
        if b == 0:
            return a
        return gcd(b, a % b)

    ans = []
    for i in range(2, n + 1):
        for j in range(1, i):
            if gcd(i, j) == 1:
                ans.append('{0}/{1}'.format(j, i))
    return ans
