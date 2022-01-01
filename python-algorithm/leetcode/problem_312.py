"""312. Burst Balloons
https://leetcode.com/problems/burst-balloons/
"""
import functools
from typing import List


def max_coins(nums: List[int]) -> int:
    @functools.lru_cache(None)
    def dfs(x: int, y: int) -> int:
        if x + 1 == y:
            return 0
        ret = 0
        for i in range(x + 1, y):
            cur = positive_nums[x] * positive_nums[i] * positive_nums[y]
            ret = max(ret, cur + dfs(x, i) + dfs(i, y))
        return ret

    positive_nums = list(filter(lambda num: num > 0, nums))
    positive_nums.insert(0, 1)
    positive_nums.append(1)
    return dfs(0, len(positive_nums) - 1)
