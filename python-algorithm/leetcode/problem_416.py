"""416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/description/

Given a non-empty array nums containing only positive integers, find if the
array can be partitioned into two subsets such that the sum of elements in
both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def can_partition(self, nums: List[int]) -> bool:
        summary = sum(nums)
        target = summary // 2
        if summary != 2 * target:
            return False
        n = len(nums)
        # dp[i][j] means i-th num sum to j
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(target + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
                if j == target and dp[i][j] is True:
                    return True
        return dp[n][target]
