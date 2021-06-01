"""342. Power of Four
https://leetcode.com/problems/power-of-four/

Given an integer n, return true if it is a power of four. Otherwise, return
false.

An integer n is a power of four, if there exists an integer x such that n ==
4^x.

Example 1:
Input: n = 16
Output: true
Example 2:
Input: n = 5
Output: false
Example 3:
Input: n = 1
Output: true

Constraints:

-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def is_power_of_four(self, n: int) -> bool:
        if n < 1:
            return False
        while n:
            if n == 1:
                return True
            n, rem = divmod(n, 4)
            if rem != 0:
                return False
        return True

    def is_power_of_four2(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
    
    def is_power_of_four3(self, n: int) -> bool:
        bin_num = bin(n)
        return n > 0 and bin_num.count('1') == 1 and bin_num.count('0') % 2 == 1