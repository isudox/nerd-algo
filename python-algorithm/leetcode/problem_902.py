"""902. Numbers At Most N Given Digit Set
https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
"""
import functools
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        @functools.lru_cache(None)
        def dfs(x: int, is_less: bool) -> int:
            if x == len(nums):
                return 1
            if is_less:
                return cnt ** (len(nums) - x)
            ret = 0
            for num in digits:
                if num > nums[x]:
                    break
                if num < nums[x]:
                    ret += dfs(x + 1, True)
                else:
                    ret += dfs(x + 1, False)
            return ret

        ans = 0
        cnt = len(digits)
        nums = [_ for _ in str(n)]
        for i in range(1, len(nums)):
            ans += cnt ** i
        ans += dfs(0, False)
        return ans
