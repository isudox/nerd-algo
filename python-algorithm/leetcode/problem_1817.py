"""1817. Finding the Users Active Minutes
https://leetcode.com/problems/finding-the-users-active-minutes/
"""
from typing import List
import collections


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        store = collections.defaultdict(set)
        for i, v in logs:
            store[i].add(v)
        time_map = collections.Counter()
        for _, v in store.items():
            time_map[len(v)] += 1
        ans = [0] * k
        for i in range(k):
            ans[i] = time_map[i + 1]
        return ans
