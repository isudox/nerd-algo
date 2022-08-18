"""1224. Maximum Equal Frequency
https://leetcode.com/problems/maximum-equal-frequency/
"""
from typing import List
import collections


class Solution:
    def max_equal_freq(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        groups = collections.Counter(counter.values())
        for i in range(len(nums) - 1, -1, -1):
            if len(groups) == 1:  # [1,1,1,1] [1,2,3,4]
                if len(counter) == 1 or list(groups.keys())[0] == 1:
                    return i + 1
            if len(groups) == 2:
                cnts = groups.keys()
                cnt1, cnt2 = min(cnts), max(cnts)
                val1, val2 = groups[cnt1], groups[cnt2]
                if (cnt2 - cnt1 == 1 and val2 == 1) or (cnt1 == 1 and val1 == 1):  # [1,1,2,2,3] [1,1,1,2,2,2,9]
                    return i + 1
            cnt = counter[nums[i]]
            groups[cnt] -= 1
            if groups[cnt] == 0:
                del groups[cnt]
            if cnt > 1:
                groups[cnt - 1] += 1
            counter[nums[i]] -= 1
        return 1
