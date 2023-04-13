"""1803. Count Pairs With XOR in a Range
https://leetcode.com/problems/count-pairs-with-xor-in-a-range/
"""
import collections
from typing import List


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def helper(x: int) -> int:
            ret = 0
            counter = collections.Counter(nums)
            while x:
                if x & 1:
                    ret += sum(counter[num] * counter[(x - 1) ^ num] for num in counter)
                counter = collections.Counter({num >> 1 : counter[num] + counter[num ^ 1] for num in counter})
                x >>= 1
            return ret >> 1

        return helper(high + 1) - helper(low)
