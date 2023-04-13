"""916. Word Subsets
https://leetcode.com/problems/word-subsets/
"""
import collections
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        letters = collections.defaultdict(int)
        for w in words2:
            counter = collections.Counter(w)
            for k, cnt in counter.items():
                letters[k] = max(letters[k], cnt)
        ans = []
        for w in words1:
            ok = True
            counter = collections.Counter(w)
            for k, cnt in letters.items():
                if cnt > counter[k]:
                    ok = False
                    break
            if ok:
                ans.append(w)
        return ans
