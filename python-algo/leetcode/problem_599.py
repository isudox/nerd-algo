"""599. Minimum Index Sum of Two Lists
https://leetcode.com/problems/minimum-index-sum-of-two-lists/
"""
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        idx_sum = 2000
        store = dict()
        for i, v in enumerate(list2):
            store[v] = i
        for i, v in enumerate(list1):
            if v in store:
                tmp_sum = i + store[v]
                if tmp_sum < idx_sum:
                    idx_sum = tmp_sum
                    ans = [v]
                elif tmp_sum == idx_sum:
                    ans.append(v)
        return ans
