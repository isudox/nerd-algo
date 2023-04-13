"""447. Number of Boomerangs
https://leetcode.com/problems/number-of-boomerangs/
"""
from typing import List
import collections
from collections import Counter


class Solution:
    def number_of_boomerangs(self, points: List[List[int]]) -> int:
        def cal(a: int, b: int) -> int:
            dx = points[a][0] - points[b][0]
            dy = points[a][1] - points[b][1]
            return dx * dx + dy * dy

        def count(tuples) -> int:
            ret = 0
            for i in range(len(tuples)):
                for j in range(i + 1, len(tuples)):
                    if tuples[i][0] == tuples[j][0] or tuples[i][0] == tuples[j][1] or tuples[i][1] == tuples[j][0] or tuples[i][1] == tuples[j][1]:
                        ret += 1
            return ret

        n = len(points)
        groups = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                length = cal(i, j)
                groups[length].append((i, j))
        ans = 0
        for tuples in groups.values():
            ans += count(tuples)
        return ans * 2

    def number_of_boomerangs2(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            counter = Counter()
            for j in range(len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                d = dx * dx + dy * dy
                counter[d] += 1
            for c in counter.values():
                ans += c * (c - 1)
        return ans
