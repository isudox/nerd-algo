"""1030. Matrix Cells in Distance Order
https://leetcode.com/problems/matrix-cells-in-distance-order/

Note:

    1 <= R <= 100
    1 <= C <= 100
    0 <= r0 < R
    0 <= c0 < C
"""
from typing import List


class Solution:
    def all_cells_dist_order(self, r: int, c: int, r0: int, c0: int) -> List[List[int]]:
        """
        time complexity: O(N)
        space complexity: O(N)
        """
        longest = max(r0 + c0, r0 + c - 1 - c0, r - 1 - r0 + c0, r - 1 - r0 + c - 1 - c0)
        store = [[] for _ in range(longest + 1)]
        for row in range(r):
            for col in range(c):
                store[abs(row - r0) + abs(col - c0)].append([row, col])
        ans = []
        for ele in store:
            ans.extend(ele)
        return ans
