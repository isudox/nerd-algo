"""9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def is_palindrome(self, x: int) -> bool:
        return x >= 0 and str(x) == str(x)[::-1]
