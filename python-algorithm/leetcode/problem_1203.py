"""1203. Sort Items by Groups Respecting Dependencies
https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
"""
import collections
from typing import List


class Solution:
    def sort_items(self, n: int, m: int, group: List[int],
                   before_items: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for i in range(n):
            graph[group[i]].append(i)

        ans = []
        return ans
