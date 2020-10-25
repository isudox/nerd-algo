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


# [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
class Solution:
    def length_of_lis(self, nums: List[int]) -> int:
        def process(start: int) -> int:
            cur_len = 1
            cur_max = nums[start]
            prev = None
            for i in range(start, n):
                if nums[i] > cur_max:
                    prev = cur_max
                    cur_max = nums[i]
                    cur_len += 1
                elif nums[i] < cur_max:
                    if (prev and prev < nums[i]) or not prev:
                        cur_max = nums[i]
            return cur_len

        n = len(nums)
        if n < 2:
            return n
        ans = 0
        for x in range(n):
            if ans >= n - x:
                break
            ans = max(ans, process(x))
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.length_of_lis([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]))
    print(sol.length_of_lis([10, 9, 2, 5, 3, 4]))
    print(sol.length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
    print(sol.length_of_lis([1, 1]))
    print(sol.length_of_lis([1]))
    print(sol.length_of_lis([]))
