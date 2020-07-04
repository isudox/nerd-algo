"""152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
from typing import List


class Solution:
    def max_product(self, nums: List[int]) -> int:
        """
        dp.
        time complexity: O(N)
        space complexity: O(N)
        """
        n = len(nums)
        ans = nums[0]
        # dp[i] means the max product of subarray which end with nums[i].
        dp = [[None] * 3 for _ in range(n)]
        if nums[0] < 0:
            dp[0][0] = nums[0]
        elif nums[0] >= 0:
            dp[0][2] = nums[0]
        else:
            dp[0][1] = 0
        for i in range(1, n):
            num = nums[i]
            if num > 0:
                if dp[i - 1][2]:
                    dp[i][2] = dp[i - 1][2] * num
                else:
                    dp[i][2] = num
                if dp[i - 1][1]:
                    dp[i][1] = 0
                if dp[i - 1][0]:
                    dp[i][0] = dp[i - 1][0] * num
            if num == 0:
                dp[i][1] = 0
            if num < 0:
                if dp[i - 1][2]:
                    dp[i][0] = dp[i - 1][2] * num
                else:
                    dp[i][0] = num
                if dp[i - 1][1]:
                    dp[i][1] = 0
                if dp[i - 1][0]:
                    dp[i][2] = dp[i - 1][0] * num
            for item in dp[i]:
                if item is not None:
                    ans = max(ans, item)
        return ans

    def max_product_2(self, nums: List[int]) -> int:
        """
        dp, same as above.
        time complexity: O(N)
        space complexity: O(N)
        """
        ans = nums[0]
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        for i in range(1, n):
            max_dp[i] = max(max_dp[i - 1] * nums[i], max(nums[i], min_dp[i - 1] * nums[i]))
            min_dp[i] = min(min_dp[i - 1] * nums[i], min(nums[i], max_dp[i - 1] * nums[i]))
            ans = max(ans, max_dp[i])
        return ans

    def max_product_3(self, nums: List[int]) -> int:
        """
        dp
        time complexity: O(N)
        space complexity: O(1)
        """
        ans = nums[0]
        max_dp = [nums[0]]
        min_dp = [nums[0]]
        for i in range(1, len(nums)):
            pre_max_dp = max_dp[0]
            pre_min_dp = min_dp[0]
            max_dp[0] = max(pre_max_dp * nums[i], max(nums[i], pre_min_dp * nums[i]))
            min_dp[0] = min(pre_min_dp * nums[i], min(nums[i], pre_max_dp * nums[i]))
            ans = max(ans, max_dp[0])
        return ans
