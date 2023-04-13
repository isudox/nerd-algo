"""967. Numbers With Same Consecutive Differences
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

Return all non-negative integers of length N such that the absolute difference
between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the
number 0 itself.
For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

  Input: N = 3, K = 7
  Output: [181,292,707,818,929]
  Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

  Input: N = 2, K = 1
  Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Note:

  1 <= N <= 9
  0 <= K <= 9
"""
from typing import List


class Solution:
    def nums_same_consec_diff(self, n, k):
        def dfs(num: int, i: int) -> List[int]:
            if i >= n:
                return [num]
            ret = []
            pre = num % 10
            if k == 0:
                ret.extend(dfs(num * 10 + pre, i + 1))
                return ret
            if pre >= k:
                ret.extend(dfs(num * 10 + pre - k, i + 1))
            if pre + k < 10:
                ret.extend(dfs(num * 10 + pre + k, i + 1))
            return ret

        ans = []
        for i in range(1, 10):
            ans.extend(dfs(i, 1))
        return ans
