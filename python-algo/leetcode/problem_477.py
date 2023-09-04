"""477. Total Hamming Distance
https://leetcode.com/problems/total-hamming-distance/
"""
from typing import List


class Solution:
    def total_hamming_distance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(30):
            counter = [0, 0]
            for num in nums:
                bit = (num >> i) & 1
                counter[bit] += 1
                ans += counter[1 - bit]
        return ans

    def total_hamming_distance2(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(30):
            cnt = 0
            for num in nums:
                if (num >> i) & 1 == 1:
                    cnt += 1
            ans += cnt * (n - cnt)
        return ans
