"""67. Add Binary
https://leetcode.com/problems/add-binary/

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""


class Solution:
    def add_binary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        n = min(len_a, len_b)
        pre = 0
        ans = ''
        for i in range(n):
            cur = int(a[len_a - i - 1]) + int(b[len_b - i - 1]) + pre
            x, y = divmod(cur, 2)
            ans = str(y) + ans
            pre = x
        c = a[:len_a - n] if len_a > n else b[:len_b - n]
        if pre == 0:
            return c + ans
        return self.add_binary(c, '1') + ans

    def add_binary_1(self, a: str, b: str) -> str:
        """
        add '0' prefix to the short string.
        """
        len_a = len(a)
        len_b = len(b)
        n = max(len_a, len_b)
        if len_a > len_b:
            b = '0' * (len_a - len_b) + b
        else:
            a = '0' * (len_b - len_a) + a
        i = 0
        pre = 0
        ans = ''
        while i < n:
            cur = int(a[n - i - 1]) + int(b[n - i - 1]) + pre
            x, y = divmod(cur, 2)
            ans = str(y) + ans
            pre = x
            i += 1
        if pre:
            ans = str(pre) + ans
        return ans

    def add_binary_2(self, a: str, b: str) -> str:
        """
        turn into decimal.
        """
        len_a = len(a)
        len_b = len(b)
        int_a, int_b = 0, 0
        for i in range(len_a):
            int_a += int(a[i]) * 2 ** (len_a - 1 - i)
        for i in range(len_b):
            int_b += int(b[i]) * 2 ** (len_b - 1 - i)
        int_sum = int_a + int_b
        if int_sum == 0:
            return '0'
        ans = ''
        while int_sum:
            int_sum, left = divmod(int_sum, 2)
            ans = str(left) + ans

        return ans
