"""452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2

Example 4:
Input: points = [[1,2]]
Output: 1

Example 5:
Input: points = [[2,3],[2,3]]
Output: 1

Constraints:

0 <= points.length <= 104
points[i].length == 2
-2^31 <= xstart < xend <= 2^31 - 1
"""
from typing import List


class Solution:
    def find_min_arrow_shots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return n
        points.sort(key=lambda e: e[1])
        ans, x = n, points[0][1]
        for i in range(n - 1):
            if x < points[i + 1][0]:
                x = points[i + 1][1]
            else:
                ans -= 1
        return ans
