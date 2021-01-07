"""416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets such that
the sum of elements in both subsets is equal.

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
We can figure out what target each subset must sum to. Then, let's recursively search,
where at each call to our function, we choose which of k subsets the next value will join.
"""
from typing import List


class Solution:
    def can_partition(self, nums: List[int]) -> bool:
        summary = sum(nums)
        target = summary // 2
        if summary != 2 * target:
            return False
        nums.sort(reverse=True)
        group1, group2 = [nums[0]], []
        n = len(nums)
        for i in range(1, n):
            pass
        return False
