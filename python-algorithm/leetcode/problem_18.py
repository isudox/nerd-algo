"""18. 4Sum
https://leetcode.com/problems/4sum/
"""
from typing import List


class Solution:
    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        def two_sum(pos: int, tar: int) -> List[List[int]]:
            res = []
            visited = set()
            seen = set()
            for i in range(pos, len(nums)):
                if tar - nums[i] in visited and (tar - nums[i], nums[i]) not in seen:
                    res.append([tar - nums[i], nums[i]])
                    seen.add((tar - nums[i], nums[i]))
                else:
                    visited.add(nums[i])
            return res

        def helper(pos: int, tar: int, cnt: int) -> List[List[int]]:
            if cnt == 2:
                return two_sum(pos, tar)
            res = list()
            seen = set()
            for i in range(pos, len(nums) - cnt + 1):
                if nums[i] * cnt > tar:
                    break
                combinations = helper(i + 1, tar - nums[i], cnt - 1)
                if combinations:
                    for combination in combinations:
                        combination.insert(0, nums[i])
                        if tuple(combination) not in seen:
                            seen.add(tuple(combination))
                            res.append(combination)

            return res

        nums.sort()
        return helper(0, target, 4)
