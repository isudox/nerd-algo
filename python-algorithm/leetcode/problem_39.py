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


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    def helper(pos: int, perm: List[int], need: int):
        if need == 0:
            nonlocal ans
            ans.append(perm[:])
        for i in range(pos, len(candidates)):
            if candidates[i] > need:
                return
            perm.append(candidates[i])
            helper(i, perm, need - candidates[i])
            perm.pop()

    candidates.sort()
    ans = []
    helper(0, [], target)
    return ans
