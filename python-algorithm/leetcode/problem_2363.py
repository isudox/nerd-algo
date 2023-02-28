"""2363. Merge Similar Items
https://leetcode.com/problems/merge-similar-items/
"""
import collections
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        store = collections.defaultdict(int)
        for v, w in items1:
            store[v] += w
        for v, w in items2:
            store[v] += w
        ans = []
        for v, w in store.items():
            ans.append([v, w])
        ans.sort(key=lambda x: x[0])
        return ans
