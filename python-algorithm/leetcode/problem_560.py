"""560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of
continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""
from typing import Counter, List
import collections


def subarray_sum(nums: List[int], k: int) -> int:
    pre_sum = [0] * (len(nums) + 1)
    for i in range(1, len(pre_sum)):
        pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
    ans = 0
    memo = collections.Counter()
    # if pre_sum[j] - pre_sum[i] == k, then (i, j) is the one.
    for i in range(len(pre_sum)):
        if pre_sum[i] not in memo:
            memo[pre_sum[i]] += 1
        if pre_sum[i] - k in memo:
            ans += memo[pre_sum[i] - k]
    return ans


def subarray_sum2(self, nums: List[int], k: int) -> int:
    ans = 0
    pre_sum = 0
    counter = collections.Counter()
    counter[0] = 1
    for num in nums:
        pre_sum += num
        if pre_sum - k in counter:
            ans += counter[pre_sum - k]
        counter[pre_sum] += 1
    return ans
