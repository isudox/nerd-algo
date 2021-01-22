"""1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
"""
from typing import List


class UnionFind:
    def __init__(self, n):
        self.uf = list(range(n))
        self.rank = [1] * n
        self.n = n
        self.count = n

    def find(self, x: int) -> int:
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.uf[y] = x
        self.rank[x] += self.rank[y]
        self.count -= 1
        return True


class Solution:
    def find_critical_and_pseudo_critical_edges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        # 计算 value
        uf_std = UnionFind(n)
        value = 0
        for i in range(m):
            if uf_std.union(edges[i][0], edges[i][1]):
                value += edges[i][2]

        ans = [list(), list()]

        for i in range(m):
            # 判断是否是关键边
            uf = UnionFind(n)
            v = 0
            for j in range(m):
                if i != j and uf.union(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if uf.count != 1 or (uf.count == 1 and v > value):
                ans[0].append(edges[i][3])
                continue

            # 判断是否是伪关键边
            uf = UnionFind(n)
            uf.union(edges[i][0], edges[i][1])
            v = edges[i][2]
            for j in range(m):
                if i != j and uf.union(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if v == value:
                ans[1].append(edges[i][3])

        return ans

    def find_critical_and_pseudo_critical_edges_2(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        pass
