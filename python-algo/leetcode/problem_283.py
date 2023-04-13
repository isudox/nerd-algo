"""283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from typing import List


class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                continue
            j = i + 1
            while j < n and nums[j] == 0:
                j += 1
            if j < n:
                nums[i] = nums[j]
                nums[j] = 0

    def move_zeroes_2(self, nums: List[int]) -> None:
        store = [[] for _ in range(2)]
        for i in range(len(nums)):
            store[0].append(i) if nums[i] == 0 else store[1].append(i)
        i, j = 0, len(nums) - 1
        for idx in store[1]:
            nums[i] = nums[idx]
            i += 1
        for idx in store[0]:
            nums[j] = 0
            j -= 1


if __name__ == '__main__':
    sol = Solution()
    arr = [0, 1, 0, 3, 12]
    sol.move_zeroes_2(arr)
    print(arr)
