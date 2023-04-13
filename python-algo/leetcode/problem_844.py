"""844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:

Can you solve it in O(N) time and O(1) space?
"ab#c"
"ad#c"
"""
from typing import List


class Solution:
    def backspace_compare(self, s: str, t: str) -> bool:
        def process(text: str) -> List[str]:
            stack = []
            for c in text:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop(-1)
            return stack

        return process(s) == process(t)

    def backspace_compare_2(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        i, j = 0, 0
        while i < len_s and j < len_t:
            if s[i] == t[j]:
                i += 1
                j += 1
            elif s[i] == '#':
                pass
        return True
