"""491. Increasing Subsequences
https://leetcode.com/problems/increasing-subsequences/

Given an integer array, your task is to find all the different possible
increasing subsequences of the given array, and the length of an increasing
subsequence should be at least 2.

Example:

Input: [4, 6, 7, 7]
Output: [[4,6], [4,7], [4,6,7], [4,6,7,7], [6,7], [6,7,7], [7,7], [4,7,7]]

Constraints:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be
considered as a special case of increasing sequence.
"""
from typing import List


class Solution:
    def find_subsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return []
        all_list, store = [], {}
        for i in range(n):
            new_append = []
            for ele in all_list:
                if ele[-1] <= nums[i]:
                    new_ele = ele[:]
                    new_ele.append(nums[i])
                    new_append.append(new_ele)
            if new_append:
                all_list.extend(new_append)
            if str(nums[i]) not in store:
                all_list.append([nums[i]])
                store[str(nums[i])] = True
        ans = []
        for ele in all_list:
            if len(ele) > 1:
                key = ','.join(map(str, ele))
                if key not in store:
                    ans.append(ele)
                    store[key] = True

        return ans
