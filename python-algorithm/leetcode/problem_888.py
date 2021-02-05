"""888. Fair Candy Swap
https://leetcode.com/problems/fair-candy-swap/

Note:

    1 <= A.length <= 10000
    1 <= B.length <= 10000
    1 <= A[i] <= 100000
    1 <= B[i] <= 100000
    It is guaranteed that Alice and Bob have different total amounts of candy.
    It is guaranteed there exists an answer.
"""
from typing import List


class Solution:
    def fair_candy_swap(self, a: List[int], b: List[int]) -> List[int]:
        def helper(nums1: List[int], nums2: List[int]) -> List[int]:
            diff = (sum(nums1) - sum(nums2)) // 2
            store = set(nums1)
            for num in nums2:
                if num + diff in store:
                    return [num + diff, num]

        if len(a) < len(b):
            return helper(b, a)[::-1]
        return helper(a, b)
