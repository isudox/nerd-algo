# -*- coding: utf-8 -*-
"""961. N-Repeated Element in Size 2N Array
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

In a array A of size 2N, there are N+1 unique elements, and exactly one of
these elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3

Example 2:

Input: [2,1,2,5,3,2]
Output: 2

Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""
import collections
from typing import List


class Solution:
    def repeated_n_times(self, a: List[int]) -> int:
        size = len(a)
        assert size % 2 == 0
        d = {}
        n = size / 2
        for i in a:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
            if d[i] == n:
                return i

    def ans(self, a: List[int]) -> int:
        count = collections.Counter(a)
        for k in count:
            if count[k] > 1:
                return k

    def ans_2(self, a: List[int]) -> int:
        for k in range(1, 4):
            for i in range(len(a) - k):
                if a[i] == a[i + k]:
                    return a[i]
