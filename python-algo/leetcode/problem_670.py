"""

"""
from typing import List


class Solution:
    def maximumSwap(self, num: int) -> int:
        def helper(digits: List[int]) -> int:
            maxx = max(digits)
            if digits[0] == maxx:
                return num
            idx = 0
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] == maxx:
                    idx = i
                    break
            digits[0], digits[idx] = digits[idx], digits[0]
            ret = 0
            for d in digits:
                ret = ret * 10 + d
            return ret

        nums = list(int(d) for d in str(num))
        sorted_nums = nums[:]
        sorted_nums.sort(reverse=True)
        pos = 0
        ans = 0
        while pos < len(nums):
            if nums[pos] == sorted_nums[pos]:
                ans = ans * 10 + nums[pos]
                pos += 1
            else:
                ans = ans * (10 ** (len(nums) - pos)) + helper(nums[pos:])
                break
        return ans
