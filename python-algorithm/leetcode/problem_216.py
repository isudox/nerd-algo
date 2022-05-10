"""216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/

Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination
should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
from typing import List


class Solution:
    def combination_sum(self, k: int, n: int) -> List[List[int]]:
        def helper(start: int, target: int, m: int) -> List[List[int]]:
            if m == 1 and start <= target <= 9:
                return [[target]]
            ret = []
            for i in range(start, min(9, target - start) + 1):
                combines = helper(i + 1, target - i, m - 1)
                if len(combines) > 0:
                    for combine in combines:
                        combine.insert(0, i)
                    ret.extend(combines)
            return ret

        return helper(1, n, k)

    def combination_sum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(target: int, start: int, store: List[int]):
            for i in range(start, 10):
                if target < i:
                    break
                if len(store) == k - 1:
                    if target < 10:
                        store.append(target)
                        nonlocal ans
                        ans.append(store[:])
                        store.pop()
                    break
                store.append(i)
                backtrack(target - i, i + 1, store)
                store.pop()

        ans = []
        backtrack(n, 1, [])
        return ans
