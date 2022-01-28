"""1996. The Number of Weak Characters in the Game
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
"""
from typing import List


def number_of_weak_characters(properties: List[List[int]]) -> int:
    properties.sort(key=lambda x: (-x[0], x[1]))
    ans = 0
    max_def = 0
    for _, defence in properties:
        if max_def > defence:
            ans += 1
        else:
            max_def = defence
    return ans
