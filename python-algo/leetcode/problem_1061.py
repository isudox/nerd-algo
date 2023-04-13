"""1061. Lexicographically Smallest Equivalent String
https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
"""


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x: str) -> str:
            uf.setdefault(x, x)
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x: str, y: str):
            px, py = find(x), find(y),
            if px > py:
                uf[px] = py
            else:
                uf[py] = px

        uf = {}
        for i in range(len(s1)):
            union(s1[i], s2[i])
        ans = ''
        for c in baseStr:
            ans += find(c)
        return ans
