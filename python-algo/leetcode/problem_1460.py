"""1460. Make Two Arrays Equal by Reversing Sub-arrays
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
"""
from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter1, counter2 = Counter(arr), Counter(target)
        for k, v in counter1.items():
            if counter2[k] != v:
                return False
        return True
