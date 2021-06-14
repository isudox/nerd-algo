"""523. Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum/

Given an integer array nums and an integer k, return true if nums has a
continuous subarray of size at least two whose elements sum up to a multiple
of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n
* k. 0 is always a multiple of k.

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up
to 6.

Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose
elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 2^31 - 1
1 <= k <= 2^31 - 1
"""
from typing import List


class Solution:
    def check_subarray_sum(self, nums: List[int], k: int) -> bool:
        store = {0: -1}
        for i in range(len(nums)):
            nums[i] = (nums[i] + (nums[i - 1] if i > 0 else 0)) % k
            if nums[i] in store and i - store[nums[i]] >= 2:
                return True
            if nums[i] not in store:
                store[nums[i]] = i
        return False