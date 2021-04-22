"""363. Max Sum of Rectangle No Larger Than K
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

Given an m x n matrix matrix and an integer k, return the max sum of a
rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than
k.

Example 1:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2,
and 2 is the max number no larger than k (k = 2).

Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-10^5 <= k <= 10^5

Follow up: What if the number of rows is much larger than the number of
columns?
"""
from typing import List
from sortedcontainers import SortedList


class Solution:
    def max_sum_submatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float('-inf')
        m, n = len(matrix), len(matrix[0])
        for upper in range(m):
            col_sums = [0] * n
            for lower in range(upper, m):
                for col in range(n):
                    col_sums[col] += matrix[lower][col]
                total_set = SortedList([0])
                cur = 0
                for col_sum in col_sums:
                    cur += col_sum
                    idx = total_set.bisect_left(cur - k)
                    if idx < len(total_set):
                        ans = max(ans, cur - total_set[idx])
                    total_set.add(cur)
        return ans
