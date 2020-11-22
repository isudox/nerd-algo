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


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        store = {}
        for c in s:
            store[c] = 1 + (store[c] if c in store else 0)
        for c in t:
            if c not in store:
                return False
            if store[c] > 1:
                store[c] -= 1
            else:
                del store[c]
        if store:
            return False
        return True
