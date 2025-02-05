"""1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/
"""
from typing import List


class Solution:
    def longest_ones(self, a: List[int], k: int) -> int:
        i = j = 0
        ans = used = 0
        while j < len(a):
            if a[j] == 0:
                if used < k:
                    used += 1
                else:
                    ans = max(ans, j - i)
                    while a[i] != 0:
                        i += 1
                    i += 1
            j += 1
        return max(ans, j - i)

    def longest_ones2(self, nums: List[int], k: int) -> int:
        ans = 0
        left, cnt0 = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                cnt0 += 1
            while cnt0 > k:
                if nums[left] == 0:
                    cnt0 -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
