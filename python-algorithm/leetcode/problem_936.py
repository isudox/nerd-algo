"""936. Stamping The Sequence
https://leetcode.com/problems/stamping-the-sequence/
"""
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def check(i: int) -> bool:
            changed = False
            for j in range(k):
                if t[i + j] == '?':
                    continue
                if t[i + j] != s[j]:
                    return False
                changed = True
            if changed:
                t[i:i + k] = ['?'] * k
                ans.insert(0, i)
            return changed

        s, t = list(stamp), list(target)
        n, k = len(t), len(s)
        ans = []
        changed = True
        while changed:
            changed = False
            for i in range(n - k + 1):
                changed |= check(i)
        return ans if t == ['?'] * n else []
