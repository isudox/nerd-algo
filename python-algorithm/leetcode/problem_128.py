"""128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

Follow up: Could you implement the O(n) solution?

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

    0 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def longest_consecutive_1(self, nums: List[int]) -> int:
        """
        time complexity: O(n)
        """
        num_set = set(nums)
        ans = 0
        for num in num_set:
            if num - 1 not in num_set:
                # find the smallest num in one consecutive nums.
                cnt = 1
                cur = num
                while cur + 1 in num_set:
                    cur += 1
                    cnt += 1
                ans = max(ans, cnt)
        return ans

    def longest_consecutive_2(self, nums: List[int]) -> int:
        """
        O(n*lg(n))
        """
        if not nums:
            return 0
        nums.sort()
        length = len(nums)
        ans = 1
        i, temp = 1, 1
        while i < length:
            if nums[i] == nums[i - 1] + 1:
                temp += 1
                ans = max(ans, temp)
            elif nums[i] != nums[i - 1]:
                temp = 1
            i += 1
        return ans

    def longest_consecutive_3(self, nums: List[int]) -> int:
        # {key: num in nums, value: the consecutive length when border is num}
        hash_map = {}
        ans = 0
        for num in nums:
            if num in hash_map:
                continue
            left_length = hash_map.get(num - 1, 0)
            right_length = hash_map.get(num + 1, 0)
            cur_length = left_length + right_length + 1
            ans = max(ans, cur_length)
            hash_map[num] = cur_length
            # tip: update the left and right border
            hash_map[num - left_length] = cur_length
            hash_map[num + right_length] = cur_length
        return ans
