"""1582. Special Positions in a Binary Matrix
https://leetcode.com/problems/special-positions-in-a-binary-matrix/
"""
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check(x: int, y: int) -> bool:
            for c in range(len(mat[0])):
                if c != y and mat[x][c] == 1:
                    return False
            for r in range(len(mat)):
                if r != x and mat[r][y] == 1:
                    return False
            return True

        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if check(i, j):
                        ans += 1
        return ans
