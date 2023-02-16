"""2341. Maximum Number of Pairs in Array
https://leetcode.com/problems/maximum-number-of-pairs-in-array
"""
from typing import List
import collections


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        a = b = 0
        for num, cnt in count.items():
            a += cnt // 2
            cnt %= 2
            if cnt > 0:
                b += 1
        return [a, b]
