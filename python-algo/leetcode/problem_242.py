"""242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
from collections import Counter


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt_s, cnt_t = Counter(s), Counter(t)
        for k, v in cnt_s.items():
            if k not in cnt_t or cnt_t[k] != v:
                return False
        return True
