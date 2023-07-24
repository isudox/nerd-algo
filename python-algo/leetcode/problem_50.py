"""50. Pow(x, n)
https://leetcode.com/problems/powx-n/
"""
import functools


class Solution:
    def my_pow(self, x: float, n: int) -> float:
        if x == 1:
            return 1.0
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.my_pow(x, -n)
        res, mod = divmod(n, 2)
        ans = self.my_pow(x, res)
        # tip: it's weird, ans ** 2 results to OverflowError.
        ans = ans ** 2
        if mod:
            ans *= x
        return ans

    def myPow(self, x: float, n: int) -> float:
        @functools.cache
        def helper(m: int) -> float:
            if m == 0:
                return 1
            if m == 1:
                return x
            return helper(m // 2) * helper(m // 2)

        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        cur = 1
        while cur * 2 <= n:
            cur *= 2
        return helper(cur) * self.myPow(x, n - cur)
