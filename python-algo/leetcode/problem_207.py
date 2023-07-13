"""207. Course Schedule
https://leetcode.com/problems/course-schedule/
"""
from typing import List
import collections


class Solution:
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        requires = [0] * num_courses
        store = collections.defaultdict(list)
        for a, b in prerequisites:
            store[b].append(a)
            requires[a] += 1
        count = 0
        queue = [i for i in range(num_courses) if not requires[i]]
        while queue:
            course = queue.pop(0)
            count += 1
            if count == num_courses:
                return True
            if course in store:
                for x in store[course]:
                    requires[x] -= 1
                    if requires[x] == 0:
                        queue.append(x)
        return False
