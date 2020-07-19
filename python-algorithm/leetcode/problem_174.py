"""174. Dungeon Game
https://leetcode.com/problems/dungeon-game/
"""
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        store = [[[0] * 2 for _ in range(cols)] for _ in range(rows)]
        store[-1][-1] = []
        i, j = rows - 1, cols - 1
        
