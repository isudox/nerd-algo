"""1807. Evaluate the Bracket Pairs of a String
https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
"""
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        store = {}
        for a, b in knowledge:
            store[a] = b
        ans = ''
        i = 0
        for j in range(len(s)):
            if s[j] == '(':
                ans += s[i:j]
                i = j + 1
            elif s[j] == ')':
                cur = s[i:j]
                ans += store[cur] if cur in store else '?'
                i = j + 1
            elif j == len(s) - 1:
                ans += s[i:]
        return ans
