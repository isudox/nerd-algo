"""2029. Stone Game IX
https://leetcode.com/problems/stone-game-ix/
"""
import collections
from typing import List


def stone_game_ix(stones: List[int]) -> bool:
    n = len(stones)
    if n == 1:
        return False
    counter = collections.Counter()
    for i in range(n):
        counter[stones[i] % 3] += 1
    if counter[0] % 2 == 0:
        return counter[1] != 0 and counter[2] != 0
    return abs(counter[1] - counter[2]) > 2
