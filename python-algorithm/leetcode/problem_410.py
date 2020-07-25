"""410. Split Array Largest Sum
https://leetcode-cn.com/problems/split-array-largest-sum/

Given an array which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
from typing import List


class Solution:
    def split_array(self, nums: List[int], m: int) -> int:
        def test_it(max_sum: int) -> bool:
            cur_sum = 0
            splits = 1
            for i in range(len(nums)):
                cur_sum += nums[i]
                if cur_sum > max_sum:
                    cur_sum = nums[i]
                    splits += 1
                    if splits > m:
                        return False
            return True

        lo, hi = max(nums), sum(nums)
        if m == 1:
            return hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if test_it(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
