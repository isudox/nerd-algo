class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res, diff = sys.maxsize, sys.maxsize
        count = len(nums)
        nums.sort()
        for i in range(count - 2):
            if i > 0 and i < count -2 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, count - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                cur_diff = cur_sum - target
                if cur_diff == 0:
                    return cur_sum
                diff = diff if abs(diff) < abs(cur_diff) else cur_diff
                res = target + diff
                if cur_diff > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res