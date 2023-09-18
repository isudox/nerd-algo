"""1337. The K Weakest Rows in a Matrix
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""
import collections
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        store = [[] for _ in range(len(mat[0]) + 1)]
        for i, row in enumerate(mat):
            store[sum(row)].append(i)
        ans = []
        for i in range(len(mat[0]) + 1):
            if store[i]:
                ans.extend(store[i][:min(len(store[i]), k)])
                k -= len(store[i])
                if k <= 0:
                    break
        return ans
