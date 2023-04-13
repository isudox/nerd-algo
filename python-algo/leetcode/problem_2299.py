"""2299. Strong Password Checker II
https://leetcode.com/problems/strong-password-checker-ii/
"""


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        has_a = has_A = has_0 = has__ = False
        sp = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+')
        pre = ''
        for c in password:
            if c == pre:
                return False
            pre = c
            if not has_a and 97 <= ord(c) < 123:
                has_a = True
            if not has_A and 65 <= ord(c) < 91:
                has_A = True
            if not has_0 and '0' <= c <= '9':
                has_0 = True
            if not has__ and c in sp:
                has__ = True
        return has_a and has_A and has_0 and has__
