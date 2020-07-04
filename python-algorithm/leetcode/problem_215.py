"""215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
from typing import List


class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        def partition(left: int, right: int) -> int:
            """
            put nums[i] to the correct place.
            :param left: left index of nums[i, j]
            :param right: right index of nums[i, j]
            :return: the correct index of nums[i]
            """
            pivot = nums[left]
            i = left
            for j in range(i + 1, right + 1):
                if nums[j] > pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[left], nums[i] = nums[i], nums[left]
            return i

        left, right = 0, len(nums) - 1
        while True:
            index = partition(left, right)
            if index == k - 1:
                return nums[index]
            elif index < k - 1:
                left = index + 1
            else:
                right = index - 1
