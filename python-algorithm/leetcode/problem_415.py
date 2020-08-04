"""415. Add Strings
https://leetcode.com/problems/add-strings/

Given two non-negative integers num1 and num2 represented as string,
return the sum of num1 and num2.

Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def add_strings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        if l1 > l2:
            return self.add_strings(num2, num1)
        prev = 0
        tail = ''
        for i in range(l1):
            curr = int(num1[l1 - i - 1]) + int(num2[l2 - 1 - i]) + prev
            prev, curr = divmod(curr, 10)
            tail = str(curr) + tail
        if prev == 0:
            return num2[:l2 - l1] + tail
        if l1 == l2:
            return str(prev) + tail
        i, zeros = l2 - l1 - 1, ''
        while i >= 0 and num2[i] == '9':
            zeros += '0'
            i -= 1
        if i == -1:
            return '1' + zeros + tail
        return num2[:i] + str(int(num2[i]) + 1) + zeros + tail

    def add_strings_2(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        if l1 > l2:
            return self.add_strings_2(num2, num1)
        num1 = '0' * (l2 - l1) + num1
        prev = 0
        ans = ''
        for i in range(l2 - 1, -1, -1):
            curr = int(num1[i]) + int(num2[i]) + prev
            prev, curr = divmod(curr, 10)
            ans = str(curr) + ans
        if prev:
            return str(prev) + ans
        return ans

    def add_strings_3(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        prev = 0
        ans = ''
        for i in range(max(l1, l2)):
            a = num1[l1 - 1 - i] if 0 <= l1 - 1 - i else '0'
            b = num2[l2 - 1 - i] if 0 <= l2 - 1 - i else '0'
            prev, curr = divmod((int(a) + int(b) + prev), 10)
            ans = str(curr) + ans
        return ('1' if prev else '') + ans
