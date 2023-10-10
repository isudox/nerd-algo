"""2578. Split With Minimum Sum
https://leetcode.com/problems/split-with-minimum-sum/
"""


class Solution:
    def splitNum(self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        nums.sort()
        a = b = 0
        for i in range(0, len(nums), 2):
            a = a * 10 + nums[i]
            if i + 1 < len(nums):
                b = b * 10 + nums[i + 1]
        return a + b
