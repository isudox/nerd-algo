"""2305. Fair Distribution of Cookies
https://leetcode.com/problems/fair-distribution-of-cookies/
"""
from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dfs(i: int, cnt0: int) -> int:
            if n - i < cnt0:
                return float('inf')
            if i == n:
                return max(store)
            ret = float('inf')
            for j in range(k):
                cnt0 -= int(store[j] == 0)
                store[j] += cookies[i]
                ret = min(ret, dfs(i + 1, cnt0))
                store[j] -= cookies[i]
                cnt0 += int(store[j] == 0)
            return ret

        n = len(cookies)
        store = [0] * k
        return dfs(0, k)
