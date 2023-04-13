"""36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for c in row:
                if c == '.':
                    continue
                if c in seen:
                    return False
                seen.add(c)
        for i in range(9):
            seen = set()
            for j in range(9):
                c = board[j][i]
                if c == '.':
                    continue
                if c in seen:
                    return False
                seen.add(c)
        for i in range(3):
            for j in range(3):
                seen = set()
                for x in range(3 * i, 3 * i + 3):
                    for y in range(3 * j, 3 * j + 3):
                        c = board[x][y]
                        if c == '.':
                            continue
                        if c in seen:
                            return False
                        seen.add(c)
        return True
