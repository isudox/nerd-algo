"""
https://leetcode.cn/problems/minimum-degree-of-a-connected-trio-in-a-graph
"""
from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = [[0] * n for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            u, v = u - 1, v - 1
            graph[u][v] = 1
            graph[v][u] = 1
            degree[u] += 1
            degree[v] += 1
        ans = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j] == 1:
                    for k in range(j + 1, n):
                        if graph[i][k] == graph[j][k] == 1:
                            ans = min(ans, degree[i] + degree[j] + degree[k] - 6)
        return ans if ans < float('inf') else -1
