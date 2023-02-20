"""2347. Best Poker Hand
https://leetcode.com/problems/best-poker-hand/
"""
from typing import List
import collections

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        def is_flush() -> bool:
            ss = set(suits)
            return len(ss) == 1

        def is_pair() -> bool:
            pass
        if is_flush():
            return 'Flush'
        counter = collections.Counter(ranks)
        max_cnt = max(counter.values())
        if max_cnt >= 3:
            return 'Three of a Kind'
        if max_cnt == 2:
            return 'Pair'
        if len(counter) == 5:
            return 'High Card'
        return ''

