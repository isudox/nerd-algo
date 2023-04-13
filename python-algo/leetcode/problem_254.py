"""254. Factor Combinations
https://leetcode-cn.com/problems/factor-combinations

Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors.
You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].

Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:

Input: n = 37
Output: []
Example 4:

Input: n = 32
Output: [[2,16],[4,8],[2,2,8],[2,4,4],[2,2,2,4],[2,2,2,2,2]]

Constraints:

1 <= n <= 10^8
"""
from typing import List


class Solution:
    def get_factors(self, n: int) -> List[List[int]]:
        def dfs(start: int, product: int, combination: List[int]):
            if start >= n or product > n:
                return
            if product == n:
                ans.append(combination[:])
                return
            for i in range(start, n // product + 1):
                if n % i == 0:
                    combination.append(i)
                    dfs(i, product * i, combination)
                    combination.pop()
        ans = []
        dfs(2, 1, [])
        return ans
