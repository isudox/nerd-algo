"""1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,`1`,1,1,1,1,`1`]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1
"""
from typing import List


class Solution:
    def longest_ones(self, a: List[int], k: int) -> int:
        i = j = 0
        ans = used = 0
        while j < len(a):
            if a[j] == 0:
                if used < k:
                    used += 1
                else:
                    ans = max(ans, j - i)
                    while a[i] != 0:
                        i += 1
                    i += 1
            j += 1
        return max(ans, j - i)

    def longest_ones2(self, nums: List[int], k: int) -> int:
        ans = 0
        left, cnt0 = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                cnt0 += 1
            while cnt0 > k:
                if nums[left] == 0:
                    cnt0 -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
