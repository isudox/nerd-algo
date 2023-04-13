"""926. Flip String to Monotone Increasing
https://leetcode.com/problems/flip-string-to-monotone-increasing/
"""
import functools


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        @functools.lru_cache(None)
        def dfs(i: int, pre: str) -> int:
            if i == len(s):
                return 0
            if pre == '0' and s[i] == '0':
                ret = dfs(i + 1, s[i])
            elif pre == '0' and s[i] == '1':
                ret = min(dfs(i + 1, '1'), dfs(i + 1, '0') + 1)
            elif pre == '1' and s[i] == '0':
                ret = dfs(i + 1, '1') + 1
            else:
                ret = dfs(i + 1, '1')
            return ret

        return dfs(0, '0')
