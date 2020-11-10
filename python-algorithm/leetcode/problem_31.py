"""31. Next Permutation
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest
possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:

Input: nums = [1]
Output: [1]

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def next_permutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n < 2:
            return
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            nums.sort(reverse=False)
            return
        gt_idx, gt_val = -1, 200
        for j in range(i, n):
            if nums[i - 1] < nums[j] < gt_val:
                gt_val = nums[j]
                gt_idx = j
        nums[i - 1], nums[gt_idx] = nums[gt_idx], nums[i - 1]
        split_nums = sorted(nums[i:])
        for k in range(n - i):
            nums[k + i] = split_nums[k]
