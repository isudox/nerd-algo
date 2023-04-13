"""2351. First Letter to Appear Twice
https://leetcode.cn/problems/first-letter-to-appear-twice/
"""
import collections


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        counter = collections.Counter()
        for c in s:
            counter[c] += 1
            if counter[c] == 2:
                return c
        return ''
