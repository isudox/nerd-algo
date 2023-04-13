"""2389. Longest Subsequence With Limited Sum
https://leetcode.com/problems/longest-subsequence-with-limited-sum/
"""
import bisect
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        for q in queries:
            i = bisect.bisect_right(nums, q)
            ans.append(i)
        return ans
