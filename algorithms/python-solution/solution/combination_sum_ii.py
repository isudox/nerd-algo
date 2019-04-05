# -*- coding: utf-8 -*-
"""40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and
a target number (target), find all unique combinations in candidates where
the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
from typing import List


class Solution:
    def combination_sum2(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        ans = []
        last_pop = None
        candidates.sort()

        def backtrack(nums: List[int], targ: int, start: int, store: List[int]):
            nonlocal last_pop
            for i in range(start, len(nums)):
                num = nums[i]
                if num == last_pop:
                    continue
                if targ < num:
                    break

                store.append(num)
                if targ == num:
                    nonlocal ans
                    ans.append(store[:])
                    store.pop()
                    break

                backtrack(nums, targ - num, i + 1, store)
                last_pop = store.pop()

        backtrack(candidates, target, 0, [])

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(solution.combination_sum2([2, 5, 2, 1, 2], 5))
