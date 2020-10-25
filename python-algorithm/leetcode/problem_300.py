"""300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing
subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101],
therefore the length is 4.

Note:

There may be more than one LIS combination, it is only necessary for you
to return the length.
Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from typing import List


class Solution:
    def length_of_lis(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        if n < 2:
            return n
        for i in range(n - 1):
            cur = 1
            prev = i
            j = i + 1
            while j < n:
                if nums[j] > nums[prev]:
                    prev = j
                    cur += 1
                j += 1
            ans = max(ans, cur)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.length_of_lis([10, 9, 2, 5, 3, 4]))
    print(sol.length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
    print(sol.length_of_lis([1, 1]))
    print(sol.length_of_lis([1]))
    print(sol.length_of_lis([]))
