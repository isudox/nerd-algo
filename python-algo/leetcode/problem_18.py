"""18. 4Sum
https://leetcode.com/problems/4sum/
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(pre: int):
            num = nums[pre]
            for i in range(pre + 1, len(nums) - 2):
                if i > pre + 1 and nums[i] == nums[i - 1]:
                    continue
                k = len(nums) - 1
                for j in range(i + 1, len(nums) - 1):
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        continue
                    while j < k and num + nums[i] + nums[j] + nums[k] > target:
                        k -= 1
                    if j == k:
                        break
                    if num + nums[i] + nums[j] + nums[k] == target:
                        ans.append([num, nums[i], nums[j], nums[k]])

        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] * 4 > target:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            threeSum(i)
        return ans
