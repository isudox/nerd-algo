"""1493. Longest Subarray of 1's After Deleting One Element
https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/
"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt1 = 0
        cnt_list = []
        splits = []
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt1 += 1
            else:
                cnt_list.append(cnt1)
                splits.append(i)
                cnt1 = 0
        ans = 0
        return ans
