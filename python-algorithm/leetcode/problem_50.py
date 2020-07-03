"""50. Pow(x, n)
https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""


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
