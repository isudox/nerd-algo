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


def next_permutation(nums: List[int]) -> None:
    n = len(nums)
    if n < 2:
        return
    i = n - 1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1
    if i == 0:
        nums.sort()
        return
    for j in range(n - 1, i - 1, -1):
        if nums[i - 1] < nums[j]:
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            break
    l, r = i, n - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1


def next_permutation2(nums: List[int]) -> None:
    i = len(nums) - 1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1
    if i == 0:
        nums.sort()
        return
    switch = i
    for j in range(i, len(nums)):
        if nums[j] > nums[i - 1]:
            if nums[j] < nums[switch]:
                switch = j
    nums[i - 1], nums[switch] = nums[switch], nums[i - 1],
    sorted_nums = sorted(nums[i:])
    for k in range(len(sorted_nums)):
        nums[i + k] = sorted_nums[k]
