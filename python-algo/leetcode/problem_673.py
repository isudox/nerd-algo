"""673. Number of Longest Increasing Subsequence
https://leetcode.com/problems/number-of-longest-increasing-subsequence/
"""
from typing import List


class Solution:
    def find_number_of_lis(self, nums: List[int]) -> int:
        lis, cnt = 0, 0
        dp = [[0, 0] for _ in nums]
        for i in range(len(nums)):
            dp[i] = [1, 1]
            for j in range(i):
                if nums[i] > nums[j]:
                    cur = dp[j][0] + 1
                    if cur > dp[i][0]:
                        dp[i][0] = cur
                        dp[i][1] = dp[j][1]
                    elif cur == dp[i][0]:
                        dp[i][1] += dp[j][1]
            if dp[i][0] > lis:
                lis = dp[i][0]
                cnt = dp[i][1]
            elif dp[i][0] == lis:
                cnt += dp[i][1]
        return cnt

    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1]] * len(nums)  # [size, count]
        cnt, sz = len(nums), 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    cur_sz, cur_cnt = dp[j][0] + 1, dp[j][1]
                    if cur_sz == sz:
                        cnt += cur_cnt
                    elif cur_sz > sz:
                        cnt = cur_cnt
                        sz = cur_sz
                    if cur_sz > dp[i][0]:
                        dp[i] = [cur_sz, cur_cnt]
                    elif cur_sz == dp[i][0]:
                        dp[i][1] = dp[i][1] + cur_cnt
        return cnt
