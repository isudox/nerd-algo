"""2185. Counting Words With a Given Prefix
https://leetcode.com/problems/counting-words-with-a-given-prefix/
"""
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for word in words:
            if word.startswith(pref):
                ans += 1
        return ans
