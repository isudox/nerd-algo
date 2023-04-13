"""997. Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/
"""
from typing import List


def find_judge(n: int, trust: List[List[int]]) -> int:
    store = list(range(n + 1))
    for t0, t1, in trust:
        store[t1] += t0
        store[t0] -= t1
    total = (1 + n) * n // 2
    for k, v in enumerate(store):
        if v == total:
            return k
    return -1
