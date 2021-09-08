"""848. Shifting Letters
https://leetcode.com/problems/shifting-letters/
"""
from typing import List


class Solution:
    def shifting_letters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        ans = ''
        for i, shift in enumerate(shifts):
            x = ord(s[i]) + shift % 26
            if x > 122:
                x -= 26
            ans += chr(x)
        return ans
