"""90. Subsets II
https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
import copy
from typing import List


class Solution:

    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:

        def frequency(collection: List[int], target: int) -> int:
            res = 0
            for i in collection:
                if i == target:
                    res += 1
            return res

        if not nums:
            return [[]]
        pre_nums = nums[:len(nums) - 1]
        pre_ans = self.subsets_with_dup(pre_nums)
        ans = copy.deepcopy(pre_ans)
        is_dup = nums[-1] in pre_nums
        for ele in pre_ans:
            if is_dup:
                # key tip: if previous list contains N num
                # and N < frequency of num in previous nums, then abandon it
                if frequency(ele, nums[-1]) < frequency(pre_ans[-1], nums[-1]):
                    continue
            ans.append(ele + [nums[-1]])
        return ans
