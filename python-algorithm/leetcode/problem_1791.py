"""1791. Find Center of Star Graph
https://leetcode.com/problems/find-center-of-star-graph/
"""
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        candidates = edges[0]
        for u, v in edges:
            if u != candidates[0] and v != candidates[1]:
                return candidates[1]
            if u != candidates[0] and u != candidates[1]:
                return candidates[0]
        return 0
