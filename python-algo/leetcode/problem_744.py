"""744. Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"""
import collections
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        counter = collections.Counter(letters)
        for i in range(1, 26):
            pos = ord(target) + i
            if pos > 122:
                pos -= 26
            ch = chr(pos)
            if counter[ch] > 0:
                return ch
        return ''
