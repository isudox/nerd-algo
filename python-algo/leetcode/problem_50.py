"""50. Pow(x, n)
https://leetcode.com/problems/powx-n/
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        n, m = divmod(n, 2)
        return self.myPow(x * x, n) * (1 if m == 0 else x)
