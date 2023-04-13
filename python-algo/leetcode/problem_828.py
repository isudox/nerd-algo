"""828. Count Unique Characters of All Substrings of a Given String
https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
"""
import collections


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        store = collections.defaultdict(list)
        for i, c in enumerate(s):
            store[c].append(i)
        ans = 0
        for positions in store.values():
            positions = [-1] + positions + [len(s)]
            for i in range(1, len(positions) - 1):
                ans += (positions[i] - positions[i - 1]) * (positions[i + 1] - positions[i])
        return ans
