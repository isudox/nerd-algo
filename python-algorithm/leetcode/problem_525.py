"""


Given a binary array nums, return the maximum length of a contiguous subarray
with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number
of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
number of 0 and 1.

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""
from typing import List


class Solution:
    def find_max_length(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = (1 if nums[i] == 1 else -1) + (nums[i - 1] if i > 0 else 0)
        store = {0: -1}
        ans = 0
        for i in range(len(nums)):
            if nums[i] in store:
                ans = max(ans, i - store[nums[i]])
            else:
                store[nums[i]] = i
        return ans
