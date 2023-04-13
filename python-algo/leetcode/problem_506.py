"""506. Relative Ranks
https://leetcode.com/problems/relative-ranks/
"""
from typing import List


def find_relative_ranks(score: List[int]) -> List[str]:
    n = len(score)
    positions = {}
    for i, s in enumerate(score):
        positions[s] = i
    ans = [''] * n
    score.sort(reverse=True)
    for i, s in enumerate(score):
        pos = positions[s]
        if i == 0:
            ans[pos] = 'Gold Medal'
        elif i == 1:
            ans[pos] = 'Silver Medal'
        elif i == 2:
            ans[pos] = 'Bronze Medal'
        else:
            ans[pos] = str(i + 1)
    return ans
