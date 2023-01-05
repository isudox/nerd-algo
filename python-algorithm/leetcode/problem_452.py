"""452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
"""
from typing import List


def find_min_arrow_shots(points: List[List[int]]) -> int:
    n = len(points)
    points.sort(key=lambda e: e[1])
    ans, x = n, points[0][1]
    for i in range(n - 1):
        if x < points[i + 1][0]:
            x = points[i + 1][1]
        else:
            ans -= 1
    return ans


def find_min_arrow_shots_2(points: List[List[int]]) -> int:
    points.sort(key=lambda p: p[1])
    ans = 1
    edge = points[0][1]
    for i in range(1, len(points)):
        if edge < points[i][0]:
            ans += 1
            edge = points[i][1]
    return ans
