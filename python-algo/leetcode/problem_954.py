"""954. Array of Doubled Pairs
https://leetcode.com/problems/array-of-doubled-pairs/
"""
import bisect
from typing import List


class Solution:
    def can_reorder_doubled(self, arr: List[int]) -> bool:
        odd_nums, even_nums = [], []
        for num in arr:
            if num % 2 == 0:
                even_nums.append(num)
            else:
                odd_nums.append(num)
        even_nums.sort()
        for odd_num in odd_nums:
            even_num = 2 * odd_num
            pos = bisect.bisect_left(even_nums, even_num)
            if even_nums[pos] != even_num:
                return False
        return False
