"""387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and
return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

Note: You may assume the string contains only lowercase English letters.
"""


class Solution:
    def first_uniq_char(self, s: str) -> int:
        store = {}
        for c in s:
            store[c] = 1 if c not in store else (1 + store[c])
        for i in range(len(s)):
            if store[s[i]] == 1:
                return i
        return -1
