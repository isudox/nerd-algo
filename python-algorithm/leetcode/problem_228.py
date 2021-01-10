"""228. Summary Ranges
https://leetcode.com/problems/summary-ranges/
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        nums.append(nums[-1] + 2)
        n = len(nums)
        pre, cnt = nums[0], 1
        for i in range(1, n):
            if nums[i] == pre + 1:
                pre = nums[i]
                cnt += 1
            else:
                if cnt == 1:
                    ans.append(str(pre))
                else:
                    ans.append(str(pre - cnt + 1) + '->' + str(pre))
                pre, cnt = nums[i], 1
        return ans
