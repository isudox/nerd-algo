"""169. Majority Element
https://leetcode.com/problems/majority-element/

Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
import collections
from typing import List


def majority_element(nums: List[int]) -> int:
    n = len(nums) / 2
    counter = collections.Counter()
    for num in nums:
        counter[num] += 1
        if counter[num] > n:
            return num
    return 0
