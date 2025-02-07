"""1726. Tuple with Same Product
https://leetcode.com/problems/tuple-with-same-product/
"""
import collections
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        store = collections.defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                store[nums[i] * nums[j]] += 1
        ans = 0
        for v in store.values():
            ans += 4 * v * (v - 1)
        return ans
