"""1338. Reduce Array Size to The Half
https://leetcode.com/problems/reduce-array-size-to-the-half/
"""
from typing import List
import collections
import math


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        cnt_arr = []
        for num, cnt in counter.items():
            cnt_arr.append(cnt)
        cnt_arr.sort(reverse=True)
        limit = math.ceil(len(arr) / 2)
        ans = 0
        for cnt in cnt_arr:
            ans += 1
            limit -= cnt
            if limit <= 0:
                return ans
        return ans
