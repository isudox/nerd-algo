"""594. Longest Harmonious Subsequence
https://leetcode.com/problems/longest-harmonious-subsequence/
"""
import collections
from typing import List


class Solution:
    def find_lhs(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        ans = 0
        for num in nums:
            if num + 1 in counter:
                ans = max(ans, counter[num] + counter[num + 1])
        return ans
