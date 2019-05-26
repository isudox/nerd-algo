"""60. Permutation Sequence
https://leetcode.com/problems/permutation-sequence/

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.


Example 1:

Input: n = 3, k = 3
Output: "213"


Example 2:

Input: n = 4, k = 9
Output: "2314"
"""
from typing import List


class Solution:
    def get_permutation(self, n: int, k: int) -> str:
        def count(m: int):
            mul = 1
            for i in range(m, 0, -1):
                mul *= i
            return mul

        def backtrack(nums: List[int], kth: int):
            res = ""
            i, j = divmod(kth, count(len(nums) - 1))
            if j > 0:
                res += str(nums.pop(i))
                res += backtrack(nums, j)
            else:
                res += str(nums.pop(i - 1))
                res += ''.join(str(_) for _ in nums[::-1])
            return res

        return backtrack([_ for _ in range(1, n + 1)], k)
