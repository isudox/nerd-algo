"""1223. Dice Roll Simulation
https://leetcode.com/problems/dice-roll-simulation/
"""
import functools
from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(i: int, last: int, left: int) -> int:
            if i == 0:
                return 1
            ret = 0
            for j, maxx in enumerate(rollMax):
                if j != last:
                    ret += dfs(i - 1, j, maxx - 1)
                elif left:
                    ret += dfs(i - 1, j, left - 1)
            return ret % BASE

        BASE = int(1e9 + 7)
        return sum(dfs(n - 1, j, maxx - 1) for j, maxx in enumerate(rollMax)) % BASE
