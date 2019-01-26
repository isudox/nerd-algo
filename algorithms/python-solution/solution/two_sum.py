# -*- coding: utf-8 -*-


class Solution(object):

    def two_sum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in d:
                return d[target - x], i
            d[x] = i
