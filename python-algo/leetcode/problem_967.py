"""967. Numbers With Same Consecutive Differences
https://leetcode.com/problems/numbers-with-same-consecutive-differences/
"""
from typing import List


class Solution:
    def nums_same_consec_diff(self, n, k):
        def dfs(num: int, i: int) -> List[int]:
            if i >= n:
                return [num]
            ret = []
            pre = num % 10
            if k == 0:
                ret.extend(dfs(num * 10 + pre, i + 1))
                return ret
            if pre >= k:
                ret.extend(dfs(num * 10 + pre - k, i + 1))
            if pre + k < 10:
                ret.extend(dfs(num * 10 + pre + k, i + 1))
            return ret

        ans = []
        for i in range(1, 10):
            ans.extend(dfs(i, 1))
        return ans
