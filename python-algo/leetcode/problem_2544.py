"""2544. Alternating Digit Sum
https://leetcode.com/problems/alternating-digit-sum/
"""


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        op = 1
        while n:
            n, m = divmod(n, 10)
            ans += m * op
            op = -op
        return ans * (-op)
