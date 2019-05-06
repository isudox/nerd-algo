"""78. Subsets
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
import copy
from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        []: []
        [1]: [] [1]
        [1,2]: [] [1] [2] [1,2]
        [1,2,3]: [] [1] [2] [1,2] [3] [1,2,3] [1,3] [2,3]
        :param nums:
        :return:
        """
        if not nums:
            return [[]]
        pre_ans = self.subsets(nums[:len(nums) - 1])
        # key tip: deep copy and append new num.
        ans = copy.deepcopy(pre_ans)
        for ele in pre_ans:
            ans.append(ele + [nums[-1]])
        return ans
