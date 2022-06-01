"""
给出一个序列包含n个正整数的序列A，你可以从中删除若干个数，使得剩下的数字中的最大值和最小值
之差不超过x，请问最少删除多少个数字。

输入：
输入第一行仅包含两个正整数n和x，表示给出的序列的长度和给定的正整数。(1<=n<=1000,1<=x<=10000)
接下来一行有n个正整数，即这个序列，中间用空格隔开。(1<=a_i<=10000)

输出：
输出仅包含一个整数，表示最少删除的数字的数量。

示例：
    输入：2, [2, 1, 3, 2, 5]
    输出：1
"""
from typing import List


class Solution:
    def remove_num(self, x, nums: List[int]) -> int:

        def check(l: int, r: int, removed: int) -> int:
            if r - l <= 1:
                return removed
            if nums[r] - nums[l] <= x:
                return removed
            return min(check(l + 1, r, removed + 1),
                       check(l, r - 1, removed + 1))

        if len(nums) <= 1:
            return 0
        nums.sort()
        return check(0, len(nums) - 1, 0)
