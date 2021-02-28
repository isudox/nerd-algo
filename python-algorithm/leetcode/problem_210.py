"""210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/

There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai,
bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite
pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to
finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you
should have finished course 0. So the correct course order is [0,1].

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you
should have finished both courses 1 and 2. Both courses 1 and 2 should be
taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is
[0,2,1,3].

Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
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
