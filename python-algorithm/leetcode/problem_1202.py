import collections
from typing import List


class Solution:
    def smallest_string_with_swaps(self, s: str, pairs: List[List[int]]) -> str:
        class UnionFind:
            def __init__(self, n):
                self.p = list(range(n))

            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)

            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

        n = len(s)
        if n == 0:
            return s
        uf, res, m = UnionFind(n), [], collections.defaultdict(list)
        for a, b in pairs:
            uf.union(a, b)
        for i in range(n):
            m[uf.find(i)].append(s[i])
        for comp_id in m.keys():
            m[comp_id].sort(reverse=True)
        for i in range(n):
            res.append(m[uf.find(i)].pop())
        return ''.join(res)
