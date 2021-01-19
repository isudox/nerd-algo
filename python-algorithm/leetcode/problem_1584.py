"""1584. Min Cost to Connect All Points
https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array points representing integer coordinates of some points
on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
absolute value of val.

Return the minimum cost to make all points connected. All points are
connected if there is exactly one simple path between any two points.

Constraints:

    1 <= points.length <= 1000
    -10^6 <= xi, yi <= 10^6
    All pairs (xi, yi) are distinct.
"""
import collections
from typing import List


class Solution:
    def min_cost_connect_points(self, points: List[List[int]]) -> int:
        def find(x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(a: int, b: int):
            uf[find(a)] = find(b)

        n = len(points)
        if n == 1:
            return 0
        edges = collections.defaultdict()
        for i in range(n - 1):
            for j in range(i + 1, n):
                edges[tuple([i, j])] = abs(points[j][0] - points[i][0]) + \
                                       abs(points[j][1] - points[i][1])
        edges = dict(sorted(edges.items(), key=lambda e: e[1]))
        ans, count = 0, 0
        uf = list(range(n))
        for k, v in edges.items():
            if find(k[0]) != find(k[1]):
                ans += v
                union(k[0], k[1])
                count += 1
                if count == n - 1:
                    break
        return ans
