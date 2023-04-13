"""2421. Number of Good Paths
https://leetcode.com/problems/number-of-good-paths/
"""
from typing import List
from collections import Counter


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        def find(x: int) -> int:
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        ans = n = len(vals)
        f = list(range(n))
        edges = sorted([max(vals[u], vals[v]), u, v] for u, v in edges)
        counter = [Counter({vals[i]: 1}) for i in range(n)]
        for x, u, v in edges:
            fu, fv = find(u), find(v)
            cu, cv = counter[fv][x], counter[fu][x]
            ans += cu * cv
            f[fv] = fu
            counter[fu] = Counter({x: cu + cv})
        return ans
