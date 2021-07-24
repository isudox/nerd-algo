"""1893. Check if All the Integers in a Range Are Covered
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
"""
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        marked = [True] * left + [False] * (right - left + 1)
        for (i, j) in ranges:
            for k in range(i, j + 1):
                if left <= k <= right and not marked[k]:
                    marked[k] = True
        for i, v in enumerate(marked):
            if v == False:
                return False
        return True
