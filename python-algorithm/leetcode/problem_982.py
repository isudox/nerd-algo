"""982. Triples with Bitwise AND Equal To Zero
https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

Given an array of integers A, find the number of triples of indices (i, j, k)
such that:

  0 <= i < A.length
  0 <= j < A.length
  0 <= k < A.length
  A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.

Example 1:

  Input: [2,1,3]
  Output: 12
  Explanation: We could choose the following i, j, k triples:
  (i=0, j=0, k=1) : 2 & 2 & 1
  (i=0, j=1, k=0) : 2 & 1 & 2
  (i=0, j=1, k=1) : 2 & 1 & 1
  (i=0, j=1, k=2) : 2 & 1 & 3
  (i=0, j=2, k=1) : 2 & 3 & 1
  (i=1, j=0, k=0) : 1 & 2 & 2
  (i=1, j=0, k=1) : 1 & 2 & 1
  (i=1, j=0, k=2) : 1 & 2 & 3
  (i=1, j=1, k=0) : 1 & 1 & 2
  (i=1, j=2, k=0) : 1 & 3 & 2
  (i=2, j=0, k=1) : 3 & 2 & 1
  (i=2, j=1, k=0) : 3 & 1 & 2

Note:

  1 <= nums.length <= 1000
  0 <= nums[i] < 2^16
"""
from collections import defaultdict
from typing import List


class Solution:
    def count_triplets(self, a: List[int]) -> int:
        ans = 0
        di = defaultdict(int)
        for x in a:
            for y in a:
                di[x & y] += 1
        for z in a:
            for k in di.keys():
                if k & z == 0:
                    ans += di[k]
        return ans

    def count_triplets2(self, nums: List[int]) -> int:
        def count(x: int, y: int, z: int) -> int:
            if x == y == z:
                return 1
            if x == y or x == z or y == z:
                return 3
            return 6

        ans = 0
        bin_nums = [[0] * 16 for _ in range(len(nums))]
        for i in range(len(nums)):
            j = 0
            while nums[i]:
                bin_nums[i][j] = nums[i] & 1
                nums[i] = nums[i] >> 1
                j += 1

        for i in range(16):
            for j in range(len(nums)):
                pass
        return ans
