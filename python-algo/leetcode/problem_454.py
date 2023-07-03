"""454. 4Sum II
https://leetcode.com/problems/4sum-ii/
"""
from typing import List


class Solution:
    def four_sum_count(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        two_sum = {}
        ans = 0
        for n1 in a:
            for n2 in b:
                summary = n1 + n2
                two_sum[summary] = 1 + (two_sum[summary] if summary in two_sum else 0)
        for n1 in c:
            for n2 in d:
                target = -n1 - n2
                if target in two_sum:
                    ans += two_sum[target]
        return ans
