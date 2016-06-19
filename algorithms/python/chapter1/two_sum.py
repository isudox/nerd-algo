class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in d:
                return d[target - x], i
            d[x] = i