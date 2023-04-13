"""839. Similar String Groups
https://leetcode.com/problems/similar-string-groups/
"""
from typing import List


class Solution:
    def num_similar_groups(self, strs: List[str]) -> int:
        def union(x: int, y: int):
            fx, fy = find(x), find(y)
            if rank[fx] < rank[fy]:
                fx, fy = fy, fx
            uf[fy] = fx
            rank[fx] += rank[fy]

        def find(x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def is_similar(w1: str, w2: str) -> bool:
            limit = 2
            for k in range(m):
                if w1[k] != w2[k]:
                    limit -= 1
                    if limit < 0:
                        return False
            return True

        n, m = len(strs), len(strs[0])
        uf, rank, = list(range(n)), [1] * n
        for i in range(n - 1):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    union(i, j)
        groups = dict()
        ans = 0
        for i in range(n):
            root = find(i)
            if root not in groups:
                ans += 1
                groups[root] = True
        return ans
