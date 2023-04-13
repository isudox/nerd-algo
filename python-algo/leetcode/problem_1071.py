"""1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        m, n = len(str1), len(str2)
        if m < n:
            return self.gcdOfStrings(str2, str1)
        if str1[:n] != str2:
            return ''
        return self.gcdOfStrings(str1[n:], str2)
