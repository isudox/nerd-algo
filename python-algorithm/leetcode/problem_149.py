"""149. Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/
"""
import collections
from typing import List


class Solution:
    def max_points(self, points: List[List[int]]) -> int:
        def gcd(x: int, y: int) -> int:
            if y == 0:
                return x
            return gcd(y, x % y)

        n = len(points)
        if n <= 2:
            return n
        ans = 1
        for i in range(n):
            store = collections.defaultdict(int)
            cur = 0
            for j in range(i + 1, n):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                d = gcd(dx, dy)
                key = '{}_{}'.format(dx // d, dy // d)
                store[key] += 1
                cur = max(cur, store[key])
            ans = max(ans, cur + 1)
        return ans
