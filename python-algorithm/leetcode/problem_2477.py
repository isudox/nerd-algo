"""2477. Minimum Fuel Cost to Report to the Capital
https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
"""
import math
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        def dfs(cur: int, par: int) -> int:
            reps = 1
            for nxt in g[cur]:
                if nxt != par:
                    reps += dfs(nxt, cur)
            if cur != 0:
                nonlocal ans
                ans += math.ceil(reps / seats)
            return reps

        n = len(roads) + 1
        g = [[] for _ in range(n)]
        for x, y in roads:
            g[x].append(y)
            g[y].append(x)
        q = []
        for i in range(1, n):
            if len(g[i]) == 1:
                q.append((i, 1))
        ans = 0
        dfs(0, -1)
        return ans
