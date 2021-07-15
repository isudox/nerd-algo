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
        # dp[0] 表示当前数不选，dp[1] 表示当前数选。从第一个数向后辗转递推
        dp = [0, nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                # 如果当前数和前一个数相等，则在前一个被选择的条件下，再选当前数。
                dp[1] += nums[i]
            elif nums[i] == nums[i - 1] + 1:
                # 如果当前数和前一个数相差 1，则一种情况是前一个数没选的条件下，选择当前数；
                # 或者在前一个数被选择的条件下，舍弃掉当前数
                temp = dp[0]
                dp[0] = max(dp)  # 舍弃掉当前数
                dp[1] = temp + nums[i]  # 选择当前数
            else:
                # 如果当前数和前一个数相差大于 1，则一种情况是前一个数已选的条件下，舍弃当前数
                # 第二种情况是，前一个数已选的条件下，选择当前数；
                # 第三种情况是，前一个数未选的条件下，选择当前数；（该情况必然非最大，不用考虑）
                # 第四种情况是，前一个数未选的条件下，舍弃当前数；（同上，非最大，不用考虑）
                dp[0] = max(dp)
                dp[1] = dp[0] + nums[i]
        return max(dp)
