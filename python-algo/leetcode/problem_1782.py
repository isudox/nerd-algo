"""1782. Count Pairs Of Nodes
"""
from typing import List
import collections
import bisect


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degree = [0] * n
        count = collections.Counter()
        for edge in edges:
            x, y = edge[0] - 1, edge[1] - 1
            if x > y:
                x, y = y, x
            degree[x] += 1
            degree[y] += 1
            count[x * n + y] += 1
        arr = sorted(degree)
        ans = []
        for q in queries:
            total = 0
            for i in range(n):
                j = bisect.bisect_right(arr, q - arr[i], i + 1)
                total += n - j
            for val, cnt in count.items():
                x, y = divmod(val, n)
                if degree[x] + degree[y] > q and degree[x] + degree[y] - cnt <= q:
                    total -= 1
            ans.append(total)
        return ans
