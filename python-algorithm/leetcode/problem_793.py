"""793. Preimage Size of Factorial Zeroes Function
https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/
"""


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def get5(x: int) -> int:
            ret = 0
            while x:
                ret += x // 5
                x //= 5
            return ret

        def f(x: int) -> int:
            lo, hi = 0, int(1e10),
            while lo < hi:
                mid = lo + (hi - lo + 1) // 2
                if get5(mid) <= x:
                    lo = mid
                else:
                    hi = mid - 1
            return hi

        if k <= 1:
            return 5
        return f(k) - f(k - 1)
