"""1819. Number of Different Subsequences GCDs
https://leetcode.com/problems/number-of-different-subsequences-gcds/
"""
import math
from typing import List


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        ans = 0
        limit = max(nums)
        valid = [False] * (limit + 1)
        for num in nums:
            valid[num] = True
        for i in range(1, limit + 1):
            tmp = 0
            for j in range(i, limit + 1, i):
                if valid[j]:
                    if tmp == 0:
                        tmp = j
                    else:
                        tmp = math.gcd(tmp, j)
                    if tmp == i:
                        ans += 1
                        break
        return ans
