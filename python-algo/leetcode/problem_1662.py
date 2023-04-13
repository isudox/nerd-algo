"""1662. Check If Two String Arrays are Equivalent
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
"""
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def concat(s: List[str]) -> str:
            ret = ''
            for e in s:
                ret += e
            return ret

        return concat(word1) == concat(word2)
