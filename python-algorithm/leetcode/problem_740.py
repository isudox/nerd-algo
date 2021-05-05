"""740. Delete and Earn
https://leetcode.com/problems/delete-and-earn/

Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points.
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by
applying such operations.

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points.
6 total points are earned.

Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.

Constraints:

1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def delete_and_earn(self, nums: List[int]) -> int:
        nums.sort()
        dp = nums[:]
        ans = dp[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dp[i] = dp[i - 1] + nums[i]
            elif nums[i] == nums[i - 1] + 1:
                for j in range(i - 2, -1, -1):
                    if nums[j] != nums[i - 1]:
                        dp[i] = max(dp[i], dp[j] + nums[i])
            else:
                for j in range(i - 1, -1, -1):
                    dp[i] = max(dp[i], dp[j] + nums[i])
            ans = max(ans, dp[i])
        return ans

    def delete_and_earn2(self, nums: List[int]) -> int:
        nums.sort()
        dp = [[0, num] for num in nums]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1] + nums[i]
            elif nums[i] == nums[i - 1] + 1:
                dp[i][0] = max(dp[i - 1])
                dp[i][1] = dp[i - 1][0] + nums[i]
            else:
                dp[i][0] = max(dp[i - 1])
                dp[i][1] = max(dp[i - 1]) + nums[i]
        return max(dp[-1])

    def delete_and_earn3(self, nums: List[int]) -> int:
        nums.sort()
        dp = [0, nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dp[1] += nums[i]
            elif nums[i] == nums[i - 1] + 1:
                temp = dp[0]
                dp[0] = max(dp)
                dp[1] = temp + nums[i]
            else:
                dp[0] = max(dp)
                dp[1] = dp[0] + nums[i]
        return max(dp)
