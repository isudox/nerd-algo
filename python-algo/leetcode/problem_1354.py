"""1354. Construct Target Array With Multiple Sums
https://leetcode.com/problems/construct-target-array-with-multiple-sums/
"""
import bisect
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total, n = 0, len(target)
        if n == 1:
            return target[0] == 1
        for num in target:
            total += num
            if num < 1:
                return False
        if total == len(target):
            return True
        target.sort()
        while total != len(target):
            maxx = target.pop()
            left = total - maxx
            if maxx - left < 1:
                return False
            orig = maxx % left
            if orig == 0:
                orig = left
            if orig < 1:
                return False
            pos = bisect.bisect_left(target, orig)
            target.insert(pos, orig)
            total = total - maxx + orig
        return True
