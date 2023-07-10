"""16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/
"""
import sys
from typing import List


class Solution:
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        res, diff = sys.maxsize, sys.maxsize
        count = len(nums)
        nums.sort()
        for i in range(count - 2):
            if 0 < i < count - 2 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, count - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                cur_diff = cur_sum - target
                if cur_diff == 0:
                    return cur_sum
                diff = diff if abs(diff) < abs(cur_diff) else cur_diff
                res = target + diff
                if cur_diff > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res

    def three_sum_closest_1(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur == target:
                    return cur
                if cur > target:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                if abs(target - cur) < abs(target - ans):
                    ans = cur
        return ans
