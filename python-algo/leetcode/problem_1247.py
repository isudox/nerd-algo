"""1247. Minimum Swaps to Make Strings Equal
https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
"""
import collections


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        cnt_diff = collections.Counter(x for x, y in zip(s1, s2) if x != y)
        d = sum(cnt_diff.values())
        return -1 if d % 2 else d // 2 + cnt_diff['x'] % 2
