"""1921. Eliminate Maximum Number of Monsters
https://leetcode.com/problems/eliminate-maximum-number-of-monsters
"""
import math
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        store = []
        for i in range(len(dist)):
            store.append(math.ceil(dist[i] / speed[i]))
        store.sort()
        t = 0
        ans = 0
        for val in store:
            if val <= t:
                break
            ans += 1
            t += 1
        return ans
