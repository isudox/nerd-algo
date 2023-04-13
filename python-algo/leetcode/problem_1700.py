"""1700. Number of Students Unable to Eat Lunch
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
"""
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            while students and students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            if not students:
                return 0
            cnt = 0
            while students[0] != sandwiches[0]:
                students.append(students[0])
                students.pop(0)
                cnt += 1
                if cnt == len(students):
                    return cnt
