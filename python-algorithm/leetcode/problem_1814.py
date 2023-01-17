"""1814. Count Nice Pairs in an Array
https://leetcode.com/problems/count-nice-pairs-in-an-array/
"""
import collections
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x: int) -> int:
            y = 0
            while x:
                y = y * 10 + x % 10
                x //= 10
            return y

        counter = collections.Counter()
        diff_nums = []
        for num in nums:
            d = num - rev(num)
            diff_nums.append(d)
            counter[d] += 1
        base = int(1e9 + 7)
        ans = 0
        for _, cnt in counter.items():
            ans = (ans + (cnt - 1) * cnt // 2) % base
        return ans
