# -*- coding: utf-8 -*-
"""967. Numbers With Same Consecutive Differences
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

Return all non-negative integers of length N such that the absolute difference
between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the
number 0 itself.
For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

  Input: N = 3, K = 7
  Output: [181,292,707,818,929]
  Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

  Input: N = 2, K = 1
  Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Note:

  1 <= N <= 9
  0 <= K <= 9
"""
from typing import List


class Solution:
    def nums_same_consec_diff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        def assemble(nums: List[int]) -> List[int]:
            nonlocal k
            new_nums = []
            for num in nums:
                next_digit = None
                if num % 10 + k < 10:
                    next_digit = num % 10 + k
                    new_nums.append(num * 10 + next_digit)
                if num % 10 - k >= 0 and (num % 10 - k) != next_digit:
                    next_digit = num % 10 - k
                    new_nums.append(num * 10 + next_digit)
            return new_nums

        if n == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        res = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for i in range(1, n):
            res = assemble(res)

        return res
