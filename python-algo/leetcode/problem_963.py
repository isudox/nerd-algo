"""963. Minimum Area Rectangle II
https://leetcode.com/problems/minimum-area-rectangle-ii/

Given a set of points in the xy-plane, determine the minimum area of any
rectangle formed from these points, with sides not necessarily parallel
to the x and y axes.

If there isn't any rectangle, return 0.

Note:
  1 <= points.length <= 50
  0 <= points[i][0] <= 40000
  0 <= points[i][1] <= 40000
  All points are distinct.
  Answers within 10^-5 of the actual value will be accepted as correct.
"""
from typing import List


class Solution:
    def min_area_free_rect(self, points: 'List[List[int]]') -> 'float':
        def distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        def is_rect(p1, p2, p3, p4):
            center = [(p1[0] + p2[0] + p3[0] + p4[0]) / 4,
                      (p1[1] + p2[1] + p3[1] + p4[1]) / 4]
            dist_1 = distance(p1, center)
            dist_2 = distance(p2, center)
            dist_3 = distance(p3, center)
            dist_4 = distance(p4, center)
            return dist_1 == dist_2 and dist_2 == dist_3 and dist_3 == dist_4

        def triangle_area(p1, p2, p3):
            return abs(
                p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p1[0] * p3[1] -
                p2[0] * p1[1] - p3[0] * p2[1]) / 2

        def rect_area(p1, p2, p3, p4):
            return triangle_area(p1, p2, p3) + triangle_area(p2, p3, p4)

        ans = float('inf')
        length = len(points)
        if length < 4:
            return 0.00000
        i = 0
        while i < length - 3:
            j = i + 1
            while j < length - 2:
                k = j + 1
                while k < length - 1:
                    l = k + 1
                    while l < length:
                        if is_rect(points[i], points[j], points[k], points[l]):
                            cur_area = rect_area(points[i], points[j],
                                                 points[k], points[l])
                            ans = min(ans, cur_area)
                        l += 1
                    k += 1
                j += 1
            i += 1
        return ans if ans < float('inf') else 0.00000
