"""952. Largest Component Size by Common Factor
https://leetcode.com/problems/largest-component-size-by-common-factor/
"""
import collections
from typing import List


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        for num in nums:
            x = 2
            while x * x <= num:
                if num % x == 0:
                    uf.union(num, x)
                    uf.union(num, num // x)
                x += 1
        counter = collections.Counter()
        for num in nums:
            counter[uf.find(num)] += 1
        return max(counter.values())


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        x, y = self.find(x), self.find(y),
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        self.rank[x] += self.rank[y]
