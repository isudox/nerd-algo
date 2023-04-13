"""1787. Make the XOR of All Segments Equal to Zero
https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

You are given an array nums and an integer k. The XOR of a segment
[left, right] where left <= right is the XOR of all the elements with indices
between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR
nums[right].

Return the minimum number of elements to change in the array such that the
XOR of all segments of size k is equal to zero.

Example 1:

Input: nums = [1,2,0,3,0], k = 1
Output: 3
Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].

Example 2:

Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
Output: 3
Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to
[3,4,7,3,4,7,3,4,7].

Example 3:

Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
Output: 3
Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to
[1,2,3,1,2,3,1,2,3].

Constraints:

1 <= k <= nums.length <= 2000
0 <= nums[i] < 2^10
"""
from typing import List
from collections import Counter


class Solution:
    def min_changes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[n] * 1024 for _ in range(k)]
        g = [n] * k
        for i in range(k):
            counter = Counter()
            size = 0
            for j in range(i, n, k):
                counter[nums[j]] += 1
                size += 1
            for j in range(1024):
                if i == 0:
                    dp[i][j] = min(dp[i][j], size - counter[j])
                    g[i] = min(g[i], dp[i][j])
                else:
                    dp[i][j] = g[i - 1] + size
                    for x, cnt in counter.items():
                        dp[i][j] = min(dp[i][j], dp[i - 1][x ^ j] + size - cnt)
                    g[i] = min(g[i], dp[i][j])
        return dp[-1][0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.min_changes([3, 4, 5, 2, 1, 7, 3, 4, 7], 3))
    print(sol.min_changes([1, 2, 4, 1, 2, 5, 1, 2, 6], 3))
    print(sol.min_changes([1, 2, 0, 3, 0], 3))
