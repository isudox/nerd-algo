"""344. Reverse String
https://leetcode.com/problems/reverse-string/
"""
from typing import List


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
