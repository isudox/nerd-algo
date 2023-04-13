"""290. Word Pattern
https://leetcode.com/problems/word-pattern/

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lower-case English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        map1, map2 = {}, {}
        n = len(words)
        for i in range(n):
            word, p = words[i], pattern[i]
            if p not in map1:
                map1[p] = word
            elif word != map1[p]:
                return False
            if word not in map2:
                map2[word] = p
            elif p != map2[word]:
                return False
        return True
