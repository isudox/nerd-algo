"""1345. Jump Game IV
https://leetcode.com/problems/jump-game-iv/
"""
import collections
from typing import List


def min_jumps(arr: List[int]) -> int:
    n = len(arr)
    if n == 1:
        return 0
    store = collections.defaultdict(list)
    for i, v in enumerate(arr):
        store[v].append(i)
    q = [0]
    visited = [False] * n
    visited[0] = True
    cnt = 0
    while q:
        next_q = []
        for pos in q:
            if pos == n - 1:
                return cnt
            for next_pos in store[arr[pos]]:
                if not visited[next_pos]:
                    visited[next_pos] = True
                    next_q.append(next_pos)
            for next_pos in [pos - 1, pos + 1]:
                if 0 <= next_pos < n and not visited[next_pos]:
                    visited[next_pos] = True
                    next_q.append(next_pos)
            store[arr[pos]].clear()
        q = next_q
        cnt += 1
    return cnt
