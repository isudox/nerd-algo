"""1078. Occurrences After Bigram
https://leetcode.com/problems/occurrences-after-bigram/
"""
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        words = text.split(' ')
        for i in range(len(words) - 1):
            if words[i] == first and words[i + 1] == second:
                if i + 2 < len(words):
                    ans.append(words[i + 2])
        return ans
