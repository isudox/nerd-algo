"""300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing
subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101],
therefore the length is 4.

Note:

There may be more than one LIS combination, it is only necessary for you
to return the length.
Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from typing import List


class Solution:
    def length_of_lis(self, nums: List[int]) -> int:
        # TODO
        result = 0

        def test(minimum: int, index: int, pre_len: int) -> int:
            nonlocal result
            for i in range(index, len(nums)):
                if nums[i] > minimum:
                    result = max(result, test(nums[i], i + 1, pre_len + 1))
            return result

        return test(0)
