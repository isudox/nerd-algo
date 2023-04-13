from typing import List


class Solution:
    def max_frequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        need_area = 0
        ans = 1
        l = 0
        for r in range(1, len(nums)):
            need_area += (nums[r] - nums[r - 1]) * (r - l)
            while need_area > k:
                need_area -= nums[r] - nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
