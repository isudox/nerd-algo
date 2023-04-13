"""539. Minimum Time Difference
https://leetcode.com/problems/minimum-time-difference/submissions/
"""
from typing import List


def find_min_difference(time_points: List[str]) -> int:
    def helper(t1: str, t2: str) -> int:
        h1, m1 = t1.split(":")
        h2, m2 = t2.split(":")
        dh, dm = int(h2) - int(h1), int(m2) - int(m1)
        ret = dh * 60 + dm
        return ret if ret < 720 else 1440 - ret

    time_points.sort()
    ans = helper(time_points[0], time_points[-1])
    for i in range(1, len(time_points)):
        ans = min(ans, helper(time_points[i - 1], time_points[i]))
    return ans
