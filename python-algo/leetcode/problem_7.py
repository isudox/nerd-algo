"""7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or
unsigned).

Example 1:
Input: x = 123
Output: 321
Example 2:
Input: x = -123
Output: -321
Example 3:
Input: x = 120
Output: 21
Example 4:
Input: x = 0
Output: 0

Constraints:

-2^31 <= x <= 2^31 - 1
"""



class Solution:
    def reverse(self, x: int) -> int:
        maxsize = 2 ** 31 - 1
        if x < 0:
            return -self.reverse(-x)
        string = str(x)
        reversed_string = string[::-1]
        ans = 0
        for c in reversed_string:
            ans = ans * 10 + int(c)
            if ans > maxsize:
                return 0
        return ans

    def reverse2(self, x: int) -> int:
        if x < 0:
            return -self.reverse2(-x)
        ans = 0
        maxsize = 2 ** 31 - 1
        while x != 0:
            x, y = divmod(x, 10)
            ans = ans * 10 + y
        return ans if ans <= maxsize else 0
