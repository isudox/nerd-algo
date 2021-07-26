"""1713. Minimum Operations to Make a Subsequence
https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/
"""
import bisect
from typing import List


class Solution:
    def min_operations(self, target: List[int], arr: List[int]) -> int:
        mapper = dict()
        for i, num in enumerate(target):
            mapper[num] = i
        stack = list()
        for num in arr:
            if num not in mapper:
                continue
            pos = bisect.bisect_left(stack, mapper[num])
            if pos == len(stack):
                stack.append(0)
            stack[pos] = mapper[num]
        return len(target) - len(stack)
