"""974. Subarray Sums Divisible by K
https://leetcode.com/problems/subarray-sums-divisible-by-k/

Given an array A of integers, return the number of (contiguous, non-empty)
subarrays that have a sum divisible by K.

Example 1:
  Input: A = [4,5,0,-2,-3,1], K = 5
  Output: 7
  Explanation: There are 7 subarrays with a sum divisible by K = 5:
  [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


Note:
  1 <= A.length <= 30000
  -10000 <= A[i] <= 10000
  2 <= K <= 10000
"""
from typing import List


class Solution:
    def subarrays_div_by_k(self, a: 'List[int]', k: 'int') -> 'int':
        ans = 0
        summary = 0
        dic = {0: 1}
        for i in a:
            summary = (summary + i) % k
            if summary in dic:
                ans += dic[summary]
                dic[summary] += 1
            else:
                dic[summary] = 1

        return ans
