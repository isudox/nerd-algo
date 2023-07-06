"""1493. Longest Subarray of 1's After Deleting One Element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
<<<<<<< HEAD
        cur = pre = ans = 0
        for num in nums:
            if num == 1:
                cur += 1
                continue
            ans = max(ans, pre + cur)
            pre, cur = cur, 0
        ans = max(ans, pre + cur)
        return ans if ans < len(nums) else ans - 1
=======
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
>>>>>>> 21ce3a8e88ccda478bdc50d78b831fc777abbdfd
