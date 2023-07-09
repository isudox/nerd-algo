"""15. 3Sum
https://leetcode.com/problems/3sum/
"""
from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = n - 1
            for j in range(i + 1, n - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while j < k and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                if j == k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
        return ans
