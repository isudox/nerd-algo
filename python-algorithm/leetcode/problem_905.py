"""905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/

Given an array A of non-negative integers, return an array consisting of
all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:

    1 <= A.length <= 5000
    0 <= A[i] <= 5000
"""
from typing import List


class Solution:
    def sort_array_by_parity(self, a: List[int]) -> List[int]:
        n = len(a)
        ans = [-1] * n
        i, j = 0, n - 1
        for num in a:
            if num % 2 == 0:
                ans[i] = num
                i += 1
            else:
                ans[j] = num
                j -= 1
        return ans

    def sort_array_by_parity_2(self, a: List[int]) -> List[int]:
        # process in place, without extra space.
        n = len(a)
        i, j = 0, n - 1
        while i < j:
            if a[i] % 2 == 0:
                i += 1
                continue
            if a[j] % 2 == 1:
                j -= 1
                continue
            a[i], a[j] = a[j], a[i],
            i += 1
            j -= 1
        return a
