"""165. Compare Version Numbers
https://leetcode.com/problems/compare-version-numbers/
"""


class Solution:
    def compare_version(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        len1, len2 = len(nums1), len(nums2)
        if len1 < len2:
            nums1.extend(['0'] * (len2 - len1))
        elif len1 > len2:
            nums2.extend(['0'] * (len1 - len2))
        for i in range(len(nums1)):
            nums1[i] = int(nums1[i])
            nums2[i] = int(nums2[i])
        for i in range(len(nums1)):
            if nums1[i] < nums2[i]:
                return -1
            elif nums1[i] > nums2[i]:
                return 1
        return 0

