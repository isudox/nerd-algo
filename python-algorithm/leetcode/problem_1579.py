"""1579. Remove Max Number of Edges to Keep Graph Fully Traversable
https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

Alice and Bob have an undirected graph of n nodes and 3 types of edges:

    Type 1: Can be traversed by Alice only.
    Type 2: Can be traversed by Bob only.
    Type 3: Can by traversed by both Alice and Bob.

Given an array edges where edges[i] = [typei, ui, vi] represents a
bidirectional edge of type typei between nodes ui and vi, find the maximum
number of edges you can remove so that after removing the edges, the graph
can still be fully traversed by both Alice and Bob. The graph is fully
traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if it's
impossible for the graph to be fully traversed by Alice and Bob.

Constraints:

    1 <= n <= 10^5
    1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
    edges[i].length == 3
    1 <= edges[i][0] <= 3
    1 <= edges[i][1] < edges[i][2] <= n
    All tuples (type_i, u_i, v_i) are distinct.
"""
from typing import List


class Solution:
    def max_num_edges_to_remove(self, n: int, edges: List[List[int]]) -> int:
        def find(uf: List[int], x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf, uf[x])
            return uf[x]

        def union(uf: List[int], rank: List[int], x: int, y: int):
            fx, fy = find(uf, x), find(uf, y)
            if rank[fx] < rank[fy]:
                fx, fy = fy, fx
            uf[fy] = fx
            rank[fx] += rank[fy]

        uf_1, rank_1 = list(range(n + 1)), [1] * (n + 1)
        uf_2, rank_2 = list(range(n + 1)), [1] * (n + 1)
        required = 0
        for t, u, v in edges:
            need = False
            if t == 3:
                if find(uf_1, u) != find(uf_1, v):
                    union(uf_1, rank_1, u, v)
                    need = True
                if find(uf_2, u) != find(uf_2, v):
                    union(uf_2, rank_2, u, v)
                    need = True
                if need:
                    required += 1
        for t, u, v in edges:
            if t == 1 and find(uf_1, u) != find(uf_1, v):
                union(uf_1, rank_1, u, v)
                required += 1
            elif t == 2 and find(uf_2, u) != find(uf_2, v):
                union(uf_2, rank_2, u, v)
                required += 1
        if required < n - 1:
            return -1
        for i in range(1, n + 1):
            if find(uf_1, i) != find(uf_1, 1) or find(uf_2, i) != find(uf_2, 1):
                return -1
        return len(edges) - required

    def max_num_edges_to_remove_2(self, n: int, edges: List[List[int]]) -> int:
        def find(uf: List[int], x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf, uf[x])
            return uf[x]

        def union(uf: List[int], rank: List[int], x: int, y: int) -> int:
            fx, fy = find(uf, x), find(uf, y)
            if fx == fy:
                return 0
            if rank[fx] < rank[fy]:
                fx, fy = fy, fx
            uf[fy] = fx
            rank[fx] += rank[fy]
            return 1

        uf_1, rank_1 = list(range(n + 1)), [1] * (n + 1)
        uf_2, rank_2 = list(range(n + 1)), [1] * (n + 1)
        required = 0
        for t, u, v in edges:
            if t == 3 and union(uf_1, rank_1, u, v) + union(uf_2, rank_2, u, v) > 0:
                required += 1
        for t, u, v in edges:
            if t == 1 and union(uf_1, rank_1, u, v):
                required += 1
            if t == 2 and union(uf_2, rank_2, u, v):
                required += 1
        if required < n - 1:
            return -1
        for i in range(1, n + 1):
            if find(uf_1, i) != find(uf_1, 1) or find(uf_2, i) != find(uf_2, 1):
                return -1
        return len(edges) - required
