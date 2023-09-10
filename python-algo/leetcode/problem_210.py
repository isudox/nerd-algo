"""210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
"""
from typing import List
import collections


class Solution:
    def find_order(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_courses = collections.defaultdict(int)
        next_courses = collections.defaultdict(list)
        for a, b in prerequisites:
            pre_courses[a] += 1
            next_courses[b].append(a)
        learned = [i for i in range(numCourses) if i not in pre_courses]
        ans = []
        while learned:
            sz = len(learned)
            for _ in range(sz):
                cur = learned.pop()
                ans.append(cur)
                for nxt in next_courses[cur]:
                    pre_courses[nxt] -= 1
                    if not pre_courses[nxt]:
                        learned.append(nxt)
        return ans if len(ans) == numCourses else []
