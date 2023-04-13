"""231. Power of Two
https://leetcode.com/problems/power-of-two/

Given an integer n, return true if it is a power of two. Otherwise, return
false.

An integer n is a power of two, if there exists an integer x such that n ==
2^x.

Example 1:

Input: n = 1
Output: true
Explanation: 2^0 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 2^4 = 16

Example 3:

Input: n = 3
Output: false

Example 4:

Input: n = 4
Output: true

Example 5:

Input: n = 5
Output: false

Constraints:

-2^31 <= n <= 2^31 - 1
"""


class Solution:
    def is_power_of_two(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        n, rem = divmod(n, 2)
        if rem == 1:
            return False
        return self.is_power_of_two(n)

    def is_power_of_two2(self, n: int) -> bool:
        if n < 1:
            return False
        while n:
            if n == 1:
                return True
            elif n & 1 == 1:
                return False
            n >>= 1
        return True

    def is_power_of_two3(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1

    def is_power_of_two4(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

    def is_power_of_two5(self, n: int) -> bool:
        return n > 0 and (2 ** 30) % n == 0
