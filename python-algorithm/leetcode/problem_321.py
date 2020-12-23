"""321. Create Maximum Number
https://leetcode.com/problems/create-maximum-number/

Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two.
The relative order of the digits from the same array must be preserved.
Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]

Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]

Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
"""
from typing import List


class Solution:
    def get_max_seq(self, nums: List[int], k: int) -> List[int]:
        """monotonic stack"""
        stack = [0] * k
        top = -1
        remain = len(nums) - k
        for i, num in enumerate(nums):
            while top >= 0 and stack[top] < num and remain > 0:
                top -= 1
                remain -= 1
            if top < k - 1:
                top += 1
                stack[top] = num
            else:
                remain -= 1
        return stack

    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x, y = len(arr1), len(arr2)
        if x == 0:
            return arr2
        if y == 0:
            return arr1
        merged_len = x + y
        merged = list()
        index1 = index2 = 0
        for _ in range(merged_len):
            if self.compare(arr1, index1, arr2, index2) > 0:
                merged.append(arr1[index1])
                index1 += 1
            else:
                merged.append(arr2[index2])
                index2 += 1
        return merged

    def compare(self, arr1: List[int], index1: int, arr2: List[int], index2: int) -> int:
        x, y = len(arr1), len(arr2)
        while index1 < x and index2 < y:
            difference = arr1[index1] - arr2[index2]
            if difference != 0:
                return difference
            index1 += 1
            index2 += 1
        return (x - index1) - (y - index2)

    def max_number(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        ans = [0] * k
        start, end = max(0, k - n), min(k, m)
        for i in range(start, end + 1):
            seq1 = self.get_max_seq(nums1, i)
            seq2 = self.get_max_seq(nums2, k - i)
            merged_seq = self.merge(seq1, seq2)
            if self.compare(merged_seq, 0, ans, 0) > 0:
                ans = merged_seq
        return ans
