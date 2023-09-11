"""630. Course Schedule III
https://leetcode.com/problems/course-schedule-iii/
"""
from typing import List
import heapq


class Solution:
    def schedule_course(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        days = 0
        learned = []
        heapq.heapify(learned)
        for course in courses:
            days += course[0]
            heapq.heappush(learned, -course[0])
            if days > course[1]:
                days += heapq.heappop(learned)
        return len(learned)
