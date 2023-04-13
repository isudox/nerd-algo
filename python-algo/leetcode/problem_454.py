"""454. 4Sum II
https://leetcode.com/problems/4sum-ii/

Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N
where 0 ≤ N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1
and the result is guaranteed to be at most 2^31 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
from typing import List


class Solution:
    def four_sum_count(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        two_sum = {}
        ans = 0
        for n1 in a:
            for n2 in b:
                summary = n1 + n2
                two_sum[summary] = 1 + (two_sum[summary] if summary in two_sum else 0)
        for n1 in c:
            for n2 in d:
                target = -n1 - n2
                if target in two_sum:
                    ans += two_sum[target]
        return ans
