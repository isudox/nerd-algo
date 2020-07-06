"""581. Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Given an integer array, you need to find one continuous subarray that
if you only sort this subarray in ascending order, then the whole array
will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make
the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""
from typing import List


class Solution:
    def find_unsorted_subarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        start, end = -1, -1
        cur_max = nums[0]
        for i in range(1, n):
            if nums[i] < nums[i - 1] or nums[i] < cur_max:
                if start < 0:
                    start = i - 1
                while start > 0 and nums[i] < nums[start - 1]:
                    start -= 1
                end = i
            else:
                cur_max = nums[i]
        while start >= 1 and nums[-1] < nums[start - 1]:
            start -= 1
        if start == -1 and end == -1:
            return 0
        return end - start + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.find_unsorted_subarray([1, 3, 5, 2]))  # 3
    print(sol.find_unsorted_subarray([1, 3, 5, 7]))  # 0
    print(sol.find_unsorted_subarray([2, 3, 3, 2, 4]))  # 3
