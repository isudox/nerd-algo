"""1010. Pairs of Songs With Total Durations Divisible by 60
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
"""
import collections
from typing import List


def numPairsDivisibleBy60(time: List[int]) -> int:
    store = collections.defaultdict(int)
    for i, t in enumerate(time):
        store[t % 60] += 1
    ans = store[0] * (store[0] - 1) // 2 + store[30] * (store[30] - 1) // 2
    for i in range(1, 30):
        ans += store[i] * store[60 - i]
    return ans
