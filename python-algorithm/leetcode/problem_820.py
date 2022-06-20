"""820. Short Encoding of Words
https://leetcode.com/problems/short-encoding-of-words/
"""
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        n = len(words)
        for i in range(n):
            words[i] = words[i][::-1]
        words.sort()
        ans = len(words[-1]) + 1
        for i in range(1, n):
            if not words[i].startswith(words[i - 1]):
                ans += len(words[i - 1]) + 1
        return ans
