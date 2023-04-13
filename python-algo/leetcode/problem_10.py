"""10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/description/


Given an input string (s) and a pattern (p), implement regular expression
matching with support for '.' and '*'.


'.' Matches any single character.
'*' Matches zero or more of the preceding element.


The matching should cover the entire input string (not partial).

Note:


s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like
. or *.


Example 1:


Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".


Example 2:


Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
by repeating 'a' once, it becomes "aa".


Example 3:


Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


Example 4:


Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
it matches "aab".


Example 5:


Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:
    def is_match(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        if p_len == 0:
            return s_len == 0
        if p_len == 1:
            if p[0] == ".":
                return s_len == 1
            return s == p
        if p[1] == "*":
            if self.is_match(s, p[2:]):
                return True
            if s_len > 0 and (p[0] == "." or s[0] == p[0]):
                return self.is_match(s[1:], p)
            return False
        else:
            if s_len > 0 and (p[0] == "." or s[0] == p[0]):
                return self.is_match(s[1:], p[1:])
            return False
