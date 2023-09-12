"""1462. Course Schedule IV
https://leetcode.com/problems/course-schedule-iv
"""
import collections
import functools
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        @functools.cache
        def dfs(x, y) -> bool:
            if x not in nxt_map or y not in pre_map:
                return False
            for nxt in nxt_map[x]:
                if nxt == y or dfs(nxt, y):
                    return True
            return False

        pre_map = collections.defaultdict(list)
        nxt_map = collections.defaultdict(list)
        for a, b in prerequisites:
            pre_map[b].append(a)
            nxt_map[a].append(b)
        return [dfs(u, v) for u, v in queries]
