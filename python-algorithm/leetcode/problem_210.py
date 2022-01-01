"""210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
"""
from typing import List
import collections


class Solution:
    def find_order(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        pre_courses = collections.defaultdict(set)
        next_courses = collections.defaultdict(set)
        for p in prerequisites:
            pre_courses[p[0]].add(p[1])
            next_courses[p[1]].add(p[0])
        learned = []
        for i in range(n):
            if i not in pre_courses:
                learned.append(i)
        ans = []
        while learned:
            m = len(learned)
            for i in range(m):
                i = learned.pop()
                ans.append(i)
                for next_course in next_courses[i]:
                    pre_courses[next_course].remove(i)
                    if not pre_courses[next_course]:
                        learned.append(next_course)
        return ans if len(ans) == n else []
