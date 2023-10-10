from typing import List


# [-2,0,2], "RLL", 3 -> 8
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        ans, base = 0, int(1e9 + 7)
        store = {'L': [], 'R': []}
        for i in range(len(s)):
            store[s[i]].append(i)
        for i in store['L']:
            for j in store['R']:
                ans = (ans + abs(nums[i] - nums[j] - 2 * d)) % base
        return ans
