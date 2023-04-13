"""1408. String Matching in an Array
https://leetcode.com/problems/string-matching-in-an-array/
"""
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        ans = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j].find(words[i]) >= 0:
                    ans.append(words[i])
                    break
        return ans
