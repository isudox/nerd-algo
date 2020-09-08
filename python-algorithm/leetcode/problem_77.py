"""77. Combinations
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers
out of 1 ... n.

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:

Input: n = 1, k = 1
Output: [[1]]

Constraints:

1 <= n <= 20
1 <= k <= n
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = [[_] for _ in range(1, n - k + 2)]
        for i in range(2, k + 1):
            temp = []
            for comb in ans:
                for j in range(comb[-1] + 1, n + 1):
                    new_comb = comb[:]
                    new_comb.append(j)
                    temp.append(new_comb)
            ans = temp
        return ans
