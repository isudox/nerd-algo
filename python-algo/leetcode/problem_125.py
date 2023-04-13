"""125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string
as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false
"""


class Solution:
    def is_palindrome(self, s: str) -> bool:
        new_s = ''
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        n = len(new_s)
        for i in range(n):
            if new_s[i] != new_s[n - 1 - i]:
                return False
        return True

    def is_palindrome_2(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n - 1
        while i < n and j >= 0:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
