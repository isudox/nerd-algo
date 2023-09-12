"""1647. Minimum Deletions to Make Character Frequencies Unique
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
"""
import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        store = collections.Counter()
        for c, cnt in count.items():
            store[cnt] += 1
        ans = 0
        for i in range(len(s) - 1, 0, -1):
            freq = store[i]
            if freq > 1:
                ans += freq - 1
                store[i - 1] += freq - 1
        return ans
