"""378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given a n x n matrix where each of the rows and columns are sorted
in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order,
not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
from typing import List


class Solution:
    def kth_smallest_1(self, matrix: List[List[int]], k: int) -> int:
        """
        brute force
        time complexity: O(N^2 * lgN)
        space complexity: O(N^2)
        """
        li = []
        for row in matrix:
            for num in row:
                li.append(num)
        li.sort()
        return li[k - 1]

    def kth_smallest_2(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            row, col, count = n - 1, 0, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    if count > k:
                        break
                    col += 1
                else:
                    row -= 1
            if count < k:
                lo = mid + 1
            elif count > k:
                hi = mid
            else:
                lo = mid - 1
                hi = mid
        return lo
