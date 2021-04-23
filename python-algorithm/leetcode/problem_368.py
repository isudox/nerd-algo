"""368. Largest Divisible Subset
https://leetcode.com/problems/largest-divisible-subset/

Given a set of distinct positive integers nums, return the largest subset
answer such that every pair (answer[i], answer[j]) of elements in this subset
satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 10^9
All the integers in nums are unique.
"""
from typing import List
import collections


class Solution:
    def largest_divisible_subset(self, nums: List[int]) -> List[int]:
        def helper(arr: List[int]) -> List[int]:
            dp = [0] * len(arr)
            dp[0] = 1
            max_len = 1
            for i in range(1, len(arr)):
                for j in range(i - 1, -1, -1):
                    if arr[i] % arr[j] == 0:
                        dp[i] = max(dp[i], dp[j] + 1)
                        max_len = max(max_len, dp[i])
            ret = []
            n = max_len
            for i in range(n):
                find(arr, dp, max_len, ret)
                max_len -= 1
            return ret

        def find(num_list: List[int], dp_list: List[int], target: int, cur_nums: List[int]):
            for i in range(len(dp_list) - 1, -1, -1):
                if dp_list[i] == target:
                    if not cur_nums or cur_nums[0] % num_list[i] == 0:
                        cur_nums.insert(0, num_list[i])

        nums.sort()
        store = collections.defaultdict(list)
        n = len(nums)
        for i in range(n):
            is_root = True
            for v in store.values():
                if nums[i] in v:
                    is_root = False
                    break
            if not is_root:
                continue
            for j in range(i, n):
                if nums[j] % nums[i] == 0:
                    store[nums[i]].append(nums[j])
        ans = []
        for candidates in store.values():
            cur_ans = helper(candidates)
            if len(cur_ans) > len(ans):
                ans = cur_ans
        return ans
