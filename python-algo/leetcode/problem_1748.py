"""1748. Sum of Unique Elements
https://leetcode.com/problems/sum-of-unique-elements/
"""
import collections
from typing import List


def sum_of_unique(nums: List[int]) -> int:
    ans = 0
    counter = collections.Counter(nums)
    for num, cnt in counter.items():
        if cnt == 1:
            ans += num
    return ans
