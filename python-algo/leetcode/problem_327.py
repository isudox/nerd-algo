"""327. Count of Range Sum
https://leetcode.com/problems/count-of-range-sum/

Given an integer array nums, return the number of range sums that lie in
[lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between
indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.

Constraints:

    0 <= nums.length <= 10^4
"""
from typing import List
import bisect


class Solution:
    def count_range_sum(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        cur_sum = 0
        sum_arr = [0]
        for i in range(len(nums)):
            cur_sum += nums[i]
            idx_l = bisect.bisect_left(sum_arr, cur_sum - upper)
            idx_r = bisect.bisect_right(sum_arr, cur_sum - lower)
            ans += idx_r - idx_l
            idx = bisect.bisect_right(sum_arr, cur_sum)
            sum_arr.insert(idx, cur_sum)
        return ans
