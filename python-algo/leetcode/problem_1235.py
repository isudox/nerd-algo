"""1235. Maximum Profit in Job Scheduling
https://leetcode.com/problems/maximum-profit-in-job-scheduling/
"""
import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = list(range(n))
        jobs.sort(key=lambda i: endTime[i])
        dp = [[0, 0]]
        for i in jobs:
            j = bisect.bisect(dp, [startTime[i] + 1]) - 1
            if dp[j][1] + profit[i] > dp[-1][1]:
                dp.append([endTime[i], dp[j][1] + profit[i]])
        return dp[-1][1]
