"""37. Sudoku Solver
https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

  1. Each of the digits 1-9 must occur exactly once in each row.
  2. Each of the digits 1-9 must occur exactly once in each column.
  3. Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.
"""
from typing import List


class Solution:
    def solve_sudoku(self, board: List[List[str]]) -> None:
        def intersection(a: List[str], b: List[str]) -> List[str]:
            return [v for v in a if v in b]

        def backtrack(x: int, y: int) -> bool:
            table = intersection(rows[x], cols[y])
            if not table:
                return False

            pass

        rows, cols = [[str(i) for i in range(1, 10)] for _ in range(9)], [
            [str(i) for i in range(1, 10)] for _ in range(9)]
        for i in range(9):
            for num in board[i]:
                if num != '.':
                    rows[i].remove(num)
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.':
                    cols[i].remove(board[j][i])
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                table = intersection(rows[i], cols[j])
                
                backtrack(i, j)


if __name__ == '__main__':
    sol = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol.solve_sudoku(board)
