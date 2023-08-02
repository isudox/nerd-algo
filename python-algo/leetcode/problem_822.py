"""822. Card Flipping Game
https://leetcode.com/problems/card-flipping-game/
"""
import collections
from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        store_front = collections.defaultdict(set)
        store_back = collections.defaultdict(set)
        for i in range(len(fronts)):
            store_front[fronts[i]].add(i)
            store_back[backs[i]].add(i)
        ans = float('inf')
        for i in range(len(fronts)):
            f, b = fronts[i], backs[i]
            if not store_front[f].intersection(store_back[f]):
                ans = min(ans, f)
            if not store_front[b].intersection(store_back[b]):
                ans = min(ans, b)
        return ans if ans < float('inf') else 0
