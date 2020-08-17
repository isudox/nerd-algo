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
        len1, len2 = len(nums1), len(nums2)
        middle_l = (len1 + len2 + 1) // 2
        middle_r = (len1 + len2 + 2) // 2
        (list1, list2) = (nums1, nums2) if len1 < len2 else (nums2, nums1)

        def get_k_th(l1: int, r1: int, l2: int, r2: int, k: int) -> int:
            """
            get the Kth element of the merged array of list1[l1:r1] and list2[l2:r2].
            :param l1: left index of list1.
            :param r1: right index of list2.
            :param l2: left index of list2.
            :param r2: right index of list2.
            :param k: k th.
            :return: the Kth number.
            """
            size1 = r1 - l1 + 1
            size2 = r2 - l2 + 1
            if size1 == 0:
                return list2[l2 + k - 1]
            if k == 1:
                return min(list1[l1], list2[l2])
            i = l1 + min(size1, k // 2) - 1
            j = l2 + min(size2, k // 2) - 1
            if list1[i] > list2[j]:
                return get_k_th(l1, r1, j + 1, r2, k - (j - l2 + 1))
            else:
                return get_k_th(i + 1, r1, l2, r2, k - (i - l1 + 1))

        return (get_k_th(0, len(list1) - 1, 0, len(list2) - 1, middle_l) +
                get_k_th(0, len(list1), 0, len(list2) - 1, middle_r)) / 2
