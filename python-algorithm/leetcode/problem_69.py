"""69. Sqrt(x)
https://leetcode.com/problems/sqrtx/

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a
non-negative integer.

Since the return type is an integer, the decimal digits are truncated and
only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


class Solution:
    def my_sqrt(self, x: int) -> int:
        """
        It takes much time.
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(1, x):
            temp = x // i
            square = temp ** 2
            if square == x:
                return temp
            elif square < x:
                return temp

    def my_sqrt_1(self, x: int) -> int:
        def divide(l: int, r: int) -> int:
            if l ** 2 == x:
                return l
            if r ** 2 == x:
                return r
            if r - l == 1:
                return l
            temp = (l + r) // 2
            square = temp ** 2
            if square < x:
                return divide(temp, r)
            if square > x:
                return divide(l, temp)
            else:
                return temp

        return divide(0, x)
