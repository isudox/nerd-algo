"""986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/
"""
from typing import List
from typing import Optional


class Solution:
    def interval_intersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        def get_overlap(a: List[int], b: List[int]) -> Optional[List[int]]:
            if a[1] < b[0] or a[0] > b[1]:
                return None
            return [max(a[0], b[0]), min(a[1], b[1])]

        ans = []
        for i, x in enumerate(firstList):
            for j, y in enumerate(secondList):
                tmp = get_overlap(x, y)
                if tmp:
                    ans.append(tmp)
        return ans
