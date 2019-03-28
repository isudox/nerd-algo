# -*- coding: utf-8 -*-
"""39. Combination Sum
https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a target
number (target), find all unique combinations in candidates where the candidate
numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

  All numbers (including target) will be positive integers.
  The solution set must not contain duplicate combinations.

Example 1:

  Input: candidates = [2,3,6,7], target = 7,
  A solution set is:
  [
    [7],
    [2,2,3]
  ]

Example 2:

  Input: candidates = [2,3,5], target = 8,
  A solution set is:
  [
    [2,2,2,2],
    [2,3,3],
    [3,5]
  ]
"""
from typing import List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(nums: List[int], start: int, targ: int, store: List[int]):
            for i in range(start, len(nums)):
                num = nums[i]
                targ -= num
                if targ < 0:
                    break

                store.append(num)
                if targ == 0:
                    nonlocal ans
                    ans.append(store.copy())
                    store.pop()
                    break
                else:
                    backtrack(nums, i, targ, store)

                targ += num
                if store:
                    store.pop()

        backtrack(candidates, 0, target, [])

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.combination_sum([1, 2], 2))
    print(solution.combination_sum([2, 3, 6, 7], 7))
    print(solution.combination_sum([2, 3, 5], 8))
