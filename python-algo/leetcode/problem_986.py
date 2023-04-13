"""986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/
"""
import bisect
from typing import List
from typing import Optional


class Solution:
    def interval_intersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        def get_overlap(a: List[int], b: List[int]) -> Optional[List[int]]:
            if a[1] < b[0] or a[0] > b[1]:
                return None
            return [max(a[0], b[0]), min(a[1], b[1])]

        left_arr, right_arr = [], []
        for x, y in secondList:
            left_arr.append(x)
            right_arr.append(y)
        ans = []
        for arr in firstList:
            idx1 = bisect.bisect_left(right_arr, arr[0])
            idx2 = bisect.bisect_left(left_arr, arr[1])
            for i in range(idx1, idx2 + 1):
                if i < len(secondList):
                    tmp = get_overlap(arr, secondList[i])
                    if tmp:
                        ans.append(tmp)
        return ans
