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

    int x = find(i), y = find(j);    //先找到两个根节点
    if (rank[x] <= rank[y])
        fa[x] = y;
    else
        fa[y] = x;
    if (rank[x] == rank[y] && x != y)
        rank[y]++;
"""
from typing import List


class Solution:
    def min_cost_connect_points(self, points: List[List[int]]) -> int:
        def find(x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(a: int, b: int):
            fa, fb = find(a), find(b)
            if rank[fa] <= rank[fb]:
                uf[fa] = fb
            else:
                uf[fb] = fa
            if rank[fa] == rank[fb]:
                rank[fb] += 1

        n = len(points)
        if n == 1:
            return 0
        edges = list()
        for i in range(n - 1):
            for j in range(i + 1, n):
                weight = abs(points[j][0] - points[i][0]) + \
                         abs(points[j][1] - points[i][1])
                edges.append((weight, i, j))
        edges.sort(key=lambda e: e[0])
        ans, count = 0, 0
        uf, rank = list(range(n)), [1] * n
        for w, i, j in edges:
            if find(i) != find(j):
                ans += w
                union(i, j)
                count += 1
                if count == n - 1:
                    break
        return ans
