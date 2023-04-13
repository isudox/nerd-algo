"""922. Sort Array By Parity II
https://leetcode.com/problems/sort-array-by-parity-ii/

Given an array A of non-negative integers, half of the integers in A are odd,
and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd;
and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Note:

    2 <= A.length <= 20000
    A.length % 2 == 0
    0 <= A[i] <= 1000
"""
from typing import List


class Solution:
    def sort_array_by_parity_ii(self, a: List[int]) -> List[int]:
        # with extra space
        n = len(a)
        ans = [-1] * n
        even_idx, odd_idx = 0, 1
        for num in a:
            if num % 2 == 0:
                ans[even_idx] = num
                even_idx += 2
            else:
                ans[odd_idx] = num
                odd_idx += 2
        return ans

    def sort_array_by_parity_ii_2(self, a: List[int]) -> List[int]:
        # two-pointer, without extra space.
        i, j, n = 0, 1, len(a)
        while i < n - 1 and j < n:
            if a[i] % 2 == 0:
                i += 2
                continue
            if a[j] % 2 == 1:
                j += 2
                continue
            else:
                a[i], a[j] = a[j], a[i]
                i += 2
                j += 2
        return a
