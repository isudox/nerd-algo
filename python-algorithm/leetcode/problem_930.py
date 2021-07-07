import collections
from typing import List


class Solution:
    def num_subarrays_with_sum(self, nums: List[int], goal: int) -> int:
        counter = collections.Counter()
        counter[0] = 1
        pre_sum = 0
        ans = 0
        i = 0
        while i < len(nums):
            pre_sum += nums[i]
            if pre_sum - goal in counter:
                ans += counter[pre_sum - goal]
            counter[pre_sum] += 1
            i += 1
        return ans
