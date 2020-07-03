"""209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution
of which the time complexity is O(n log n).
"""
from typing import List


class Solution:
    def min_sub_arrayLen(self, s: int, nums: List[int]) -> int:
        # double pointers
        n = len(nums)
        ans = n + 1
        i, j, cur = 0, 0, 0
        move_i = False
        while i <= j < n:
            if move_i:
                cur -= nums[i - 1]
            else:
                cur += nums[j]
            if cur >= s:
                ans = min(ans, j - i + 1)
                i += 1
                move_i = True
            else:
                j += 1
                move_i = False

        return ans if ans <= n else 0
