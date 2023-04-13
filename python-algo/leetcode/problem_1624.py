"""1624. Largest Substring Between Two Equal Characters
https://leetcode.com/problems/largest-substring-between-two-equal-characters/
"""
import collections


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        store = collections.defaultdict(int)
        for i, c in enumerate(s):
            if c not in store:
                store[c] = i
            else:
                ans = max(ans, i - store[c] - 1)
        return ans
