"""312. Burst Balloons
https://leetcode.com/problems/burst-balloons/

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number
on it represented by array nums. You are asked to burst all the balloons.
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i.
After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1.
They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
from typing import List


class Solution:
    def max_coins(self, nums: List[int]) -> int:
        def burst(left: int, right: int) -> int:
            if right - left == 1:
                return 0
            if memo[left][right] > 0:
                return memo[left][right]
            ret = 0
            for i in range(left + 1, right):
                ret = max(ret, new_nums[left] * new_nums[i] * new_nums[right] +
                          burst(left, i) + burst(i, right))
            memo[left][right] = ret
            return ret

        new_nums = [1]
        for num in nums:
            if num > 0:
                new_nums.append(num)
        new_nums.append(1)
        m = len(new_nums)
        memo = [[0] * m for _ in range(m)]
        return burst(0, m - 1)
