"""303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, find the sum of the elements between indices i
and j (i ≤ j), inclusive.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array
in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... ,
nums[j]))

Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

Constraints:
0 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= i <= j < nums.length
At most 10^4 calls will be made to sumRange.
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre_sums = [-1] * len(nums)

    def sum_pre(self, i: int):
        cur_sum = 0
        k = i
        while k >= 0 and self.pre_sums[k] == -1:
            cur_sum += self.nums[k]
            k -= 1
        self.pre_sums[i] = cur_sum + (self.pre_sums[k] if k >= 0 else 0)

    def sum_range(self, i: int, j: int) -> int:
        if self.pre_sums[i] == -1:
            self.sum_pre(i)
        if self.pre_sums[j] == -1:
            self.sum_pre(j)
        return self.pre_sums[j] - self.pre_sums[i] + self.nums[i]
