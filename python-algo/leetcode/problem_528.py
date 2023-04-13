"""528. Random Pick with Weight
https://leetcode.com/problems/random-pick-with-weight/
"""
from typing import List
import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.n = sum(w)
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.w, random.randint(1, self.n))

