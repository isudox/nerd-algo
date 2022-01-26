"""2013. Detect Squares
https://leetcode.com/problems/detect-squares/
"""
import collections
from typing import List


class DetectSquares:

    def __init__(self):
        self.mapper = collections.defaultdict(collections.Counter)

    def add(self, point: List[int]) -> None:
        self.mapper[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        cnt = 0
        for ny, v in self.mapper[x].items():
            if ny == y:
                continue
            c1 = self.mapper[x][ny]
            diff = y - ny
            for nx in [x - diff, x + diff]:
                c2 = self.mapper[nx][y]
                c3 = self.mapper[nx][ny]
                cnt += c1 * c2 * c3
        return cnt
