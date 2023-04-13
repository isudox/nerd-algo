"""4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""
from typing import List


class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        x, y = divmod(n + m, 2)
        is_odd = True if y == 1 else False
        mid_l = mid_r = x
        if not is_odd:
            mid_l = mid_r - 1
        i = j = 0
        counter = -1
        ans = 0
        while i < n or j < m:
            if i == n and j < m:
                smaller = nums2[j]
                j += 1
            elif i < n and j == m:
                smaller = nums1[i]
                i += 1
            elif nums1[i] <= nums2[j]:
                smaller = nums1[i]
                i += 1
            else:
                smaller = nums2[j]
                j += 1
            counter += 1
            if counter == mid_l:
                if is_odd:
                    return smaller
                else:
                    ans = smaller
            if counter == mid_r:
                return (ans + smaller) / 2
