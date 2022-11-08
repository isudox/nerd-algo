"""1684. Count the Number of Consistent Strings
https://leetcode.com/problems/count-the-number-of-consistent-strings/
"""
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0
        for word in words:
            flag = True
            for c in word:
                if c not in allowed:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans
