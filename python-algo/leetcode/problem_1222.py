"""1222. Queens That Can Attack the King
https://leetcode.cn/problems/queens-that-can-attack-the-king
"""
from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        queen_pos = set()
        for x, y in queens:
            queen_pos.add((x, y))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for d0, d1 in dirs:
            for i in range(1, 8):
                dx, dy = king[0] + i * d0, king[1] + i * d1
                if dx < 0 or dx >= 8 or dy < 0 or dy >= 8:
                    break
                if (dx, dy) in queen_pos:
                    ans.append([dx, dy])
                    break
        return ans
