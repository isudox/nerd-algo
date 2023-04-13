"""846. Hand of Straights
https://leetcode.com/problems/hand-of-straights/
"""
import collections
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        counter = collections.Counter(hand)
        for num in hand:
            if counter[num] == 0:
                continue
            for i in range(num, num + groupSize):
                if counter[i] == 0:
                    return False
                counter[i] -= 1
        return True
