"""58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/

Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of
non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution:
    def length_of_last_word(self, s: str) -> int:
        index = len(s) - 1
        while index >= 0 and s[index] == " ":
            index -= 1
        ans = 0
        for i in range(index, -1, -1):
            if s[i] == ' ':
                break
            ans += 1
        return ans
