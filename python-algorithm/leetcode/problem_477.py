"""477. Total Hamming Distance
https://leetcode.com/problems/total-hamming-distance/

The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all
the pairs of the integers in nums.

Example 1:

Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is
0010 (just showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 +
2 + 2 = 6.

Example 2:

Input: nums = [4,14,4]
Output: 4

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
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
