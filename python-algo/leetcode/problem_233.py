"""233. Number of Digit One
https://leetcode.com/problems/number-of-digit-one/
"""


class Solution:
    def count_digit_one(self, n: int) -> int:
        def helper(x: int) -> int:
            return x * 10 ** (x - 1)

        if n == 0:
            return 0
        if n < 10:
            return 1
        sn = str(n)
        i = len(sn) - 1
        ans = helper(i) * int(sn[0]) + self.count_digit_one(int(sn[1:]))
        return ans + (10 ** i if int(sn[0]) > 1 else int(sn[1:]) + 1)
