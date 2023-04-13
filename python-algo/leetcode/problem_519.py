"""519. Random Flip Matrix
https://leetcode.com/problems/random-flip-matrix/
"""
import random
from typing import List


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.max = m * n
        self.map = dict()

    def flip(self) -> List[int]:
        r = random.randint(0, self.max - 1)
        self.max -= 1
        pos = self.map.get(r, r)
        self.map[r] = self.map.get(self.max, self.max)
        return [pos // self.n, pos % self.n]

    def reset(self) -> None:
        self.max = self.m * self.n
        self.map.clear()
