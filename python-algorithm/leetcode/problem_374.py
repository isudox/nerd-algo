"""374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/
"""


class Solution:
    def guessNumber(self, n: int) -> int:
        def guess(x: int) -> int:
            return 0

        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            ret = guess(mid)
            if ret == 0:
                return mid
            if ret == 1:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
