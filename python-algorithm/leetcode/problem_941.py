"""941. Valid Mountain Array
https://leetcode.com/problems/valid-mountain-array/

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:

Input: [2,1]
Output: false

Example 2:

Input: [3,5,5]
Output: false

Example 3:

Input: [0,3,2,1]
Output: true

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
"""
from typing import List


def valid_mountain_array(nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False
    if nums[0] >= nums[1]:
        return False
    found_peak = False
    for i in range(n - 1):
        if not found_peak:
            if nums[i] == nums[i + 1]:
                return False
            if nums[i] > nums[i + 1]:
                found_peak = True
        else:
            if nums[i] <= nums[i + 1]:
                return False
    return found_peak


def valid_mountain_array_1(nums: List[int]) -> bool:
    n = len(nums)
    i, j = 0, n - 1
    while i < n - 1 and nums[i] < nums[i + 1]:
        i += 1
    while j > 0 and nums[j] < nums[j - 1]:
        j -= 1
    return i == j and i != 0 and i != n - 1
