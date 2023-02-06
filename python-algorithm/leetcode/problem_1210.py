"""1210. Minimum Moves to Reach Target with Rotations
https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/
"""
import collections
from typing import List


# TODO
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n, ans = len(grid), 0
        q = collections.deque([(0, 0, 0)])  # tail at [0,0], head for right
        while q:
            x, y, state = q.popleft()
            if state == 0:
                pass
        return ans
