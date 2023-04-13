"""2100. Find Good Days to Rob the Bank
https://leetcode.com/problems/find-good-days-to-rob-the-bank/
"""
from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if 2 * time + 1 > n:
            return []
        if time == 0:
            return list(range(n))
        g = [0] * n
        for i in range(1, n):
            if security[i] > security[i - 1]:
                g[i] = 1
            if security[i] < security[i - 1]:
                g[i] = -1
        a = [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = a[i - 1] + (1 if g[i - 1] == 1 else 0)
        b = [0] * (n + 1)
        for i in range(1, n + 1):
            b[i] = b[i - 1] + (1 if g[i - 1] == -1 else 0)
        ans = []
        for i in range(time, n - time):
            cnt_a = a[i + 1] - a[i + 1 - time]
            cnt_b = b[i + 1 + time] - b[i + 1]
            if cnt_a == 0 and cnt_b == 0:
                ans.append(i)
        return ans
