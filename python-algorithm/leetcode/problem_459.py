"""459. Repeated Substring Pattern
https://leetcode.com/problems/repeated-substring-pattern/

Given a non-empty string check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only
and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution:
    def repeated_substring_pattern_1(self, s: str) -> bool:
        return s in (s + s)[1:-1]

    def repeated_substring_pattern(self, s: str) -> bool:
        def validate(prefix: str, start: int) -> bool:
            if start == n:
                return True
            if s[start:].startswith(prefix):
                return validate(prefix, start + len(prefix))
            else:
                return False

        n = len(s)
        for x in range(n // 2, 0, -1):
            if n % x == 0:
                if validate(s[:x], 0):
                    return True
        return False
