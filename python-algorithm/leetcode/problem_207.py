"""207. Course Schedule
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take,
labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0.
             So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0,
             and to take course 0 you should
             also have finished course 1. So it is impossible.

Constraints:

    The input prerequisites is a graph represented by a list of edges,
    not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
    1 <= numCourses <= 10^5
"""
from typing import List


class Solution:
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or not prerequisites[0]:
            return True

        in_degree = [0] * num_courses
        edges = {}
        for e in prerequisites:
            if e[1] in edges:
                edges[e[1]].append(e[0])
            else:
                edges[e[1]] = [e[0]]
            in_degree[e[0]] += 1
        count = 0
        queue = []
        for i in range(num_courses):
            if in_degree[i] == 0:
                queue.append(i)
        while queue:
            count += 1
            if count == num_courses:
                return True
            course = queue.pop(0)
            if course in edges:
                for x in edges[course]:
                    in_degree[x] -= 1
                    if in_degree[x] == 0:
                        queue.append(x)

        return False
