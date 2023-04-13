"""884. Uncommon Words from Two Sentences
https://leetcode.com/problems/uncommon-words-from-two-sentences/
"""
import collections
from typing import List


def uncommon_from_sentences(s1: str, s2: str) -> List[str]:
    ans = []
    word_cnt1 = collections.Counter(s1.split(' '))
    word_cnt2 = collections.Counter(s2.split(' '))
    for w, c in word_cnt1.items():
        if c == 1 and w not in word_cnt2:
            ans.append(w)
    for w, c in word_cnt2.items():
        if c == 1 and w not in word_cnt1:
            ans.append(w)
    return ans
