"""792. Number of Matching Subsequences
https://leetcode.com/problems/number-of-matching-subsequences/
"""
import bisect
import collections
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def check(word: str) -> bool:
            pre = -1
            for ch in word:
                if ch not in store:
                    return False
                positions = store[ch]
                if positions[-1] < pre:
                    return False
                ok = False
                idx = bisect.bisect_left(positions, pre)
                for i in range(idx, len(positions)):
                    if positions[i] > pre:
                        pre = positions[i]
                        ok = True
                        break
                if not ok:
                    return False
            return True

        store = collections.defaultdict(list)
        for i, ch in enumerate(s):
            store[ch].append(i)
        ans = 0
        for word in words:
            if check(word):
                ans += 1
        return ans
