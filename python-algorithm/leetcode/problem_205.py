"""205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
"""


class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        mapper_s, mapper_t = {}, {}
        for i in range(n):
            if s[i] not in mapper_s:
                mapper_s[s[i]] = t[i]
            elif mapper_s[s[i]] != t[i]:
                return False
            if t[i] not in mapper_t:
                mapper_t[t[i]] = s[i]
            elif mapper_t[t[i]] != s[i]:
                return False
        return True
