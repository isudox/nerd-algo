"""834. Sum of Distances in Tree
https://leetcode.com/problems/sum-of-distances-in-tree/
"""
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(cur: int, pre: int):
            for nxt in graph[cur]:
                if nxt == pre:
                    continue
                dfs(nxt, cur)
                cnt[cur] += cnt[nxt]
                ans[cur] += ans[nxt] + cnt[nxt]

        def dfs2(cur: int, pre: int):
            for nxt in graph[cur]:
                if nxt == pre:
                    continue
                ans[nxt] = ans[cur] - cnt[nxt] + n - cnt[nxt]
                dfs2(nxt, cur)

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        ans = [0] * n
        cnt = [1] * n
        dfs(0, -1)
        dfs2(0, -1)
        return ans
