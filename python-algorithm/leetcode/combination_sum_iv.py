# -*- coding: utf-8 -*-
"""377. Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/

Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive
integer target.

Example:

  nums = [1, 2, 3]
  target = 4

  The possible combination ways are:
  (1, 1, 1, 1)
  (1, 1, 2)
  (1, 2, 1)
  (1, 3)
  (2, 1, 1)
  (2, 2)
  (3, 1)

  Note that different sequences are counted as different combinations.

  Therefore the output is 7.

Follow up:

What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
from typing import List
from itertools import permutations


class Solution:
    def combination_sum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        matrix = []

        def backtrack(target: int, start: int, store: List[int]):
            nonlocal nums, matrix
            for i in range(start, len(nums)):
                num = nums[i]
                if target < num:
                    break

                if target == num:
                    store.append(num)
                    matrix.append(store[:])
                    store.pop()
                    break

                store.append(num)
                backtrack(target - num, i, store)
                store.pop()

        def count_permutation(combination: List[int]) -> int:
            num = ''.join(str(e) for e in combination)
            return len({''.join(p) for p in permutations(num)})

        backtrack(target, 0, [])
        ans = 0
        for i in matrix:
            ans += count_permutation(i)

        return ans
