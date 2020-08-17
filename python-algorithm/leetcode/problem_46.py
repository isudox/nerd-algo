"""46. Permutations
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length == 0:
            return [[]]
        ans = []
        pre_ans = self.permute(nums[:-1])
        for permutation in pre_ans:
            for i in range(length):
                temp = copy.deepcopy(permutation)
                temp.insert(i, nums[-1])
                ans.append(temp)
        return ans
