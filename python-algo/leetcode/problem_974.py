"""974. Subarray Sums Divisible by K
https://leetcode.com/problems/subarray-sums-divisible-by-k/
"""
import collections
from typing import List


class Solution:
    def subarrays_div_by_k(self, nums: List[int], k: int) -> int:
        ans = 0
        store = collections.Counter()
        store[0] = 1
        cur = 0
        for num in nums:
            cur = (cur + num) % k
            if cur in store:
                ans += store[cur]
            store[cur] += 1
        return ans
