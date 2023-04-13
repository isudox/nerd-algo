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
        if not nums:
            return [[]]
        pre_ans = self.subsets(nums[:len(nums) - 1])
        # key tip: deep copy and append new num.
        ans = copy.deepcopy(pre_ans)
        for ele in pre_ans:
            ans.append(ele + [nums[-1]])
        return ans

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(len(nums)):
            n = len(ans)
            for j in range(n):
                new_perm = ans[j][:]
                new_perm.append(nums[i])
                ans.append(new_perm)
        return ans

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        size = 1 << n
        ans = []
        for i in range(size):
            perm = []
            for j in range(n):
                bit = i & 1
                if bit == 1:
                    perm.append(nums[j])
                i = i >> 1
            ans.append(perm)
        return ans
