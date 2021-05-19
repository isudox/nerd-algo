"""37. Sudoku Solver
https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

  Each of the digits 1-9 must occur exactly once in each row.
  Each of the digits 1-9 must occur exactly once in each column.
  Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes
  of the grid.

The '.' character indicates empty cells.

Example 1:

Input: board =
[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
Output:
[["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]]

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""
from typing import List


class Solution:
    def solve_sudoku(self, board: List[List[str]]) -> None:
        def get_options(x: int, y: int) -> List[str]:
            used = [0] * 10
            for v in board[x]:
                if v != '.':
                    used[int(v)] = 1
            for i in range(9):
                if board[i][y] != '.':
                    used[int(board[i][y])] = 1
            m, n = x // 3, y // 3
            for i in range(3 * m, 3 * m + 3):
                for j in range(3 * n, 3 * n + 3):
                    if board[i][j] != '.':
                        used[int(board[i][j])] = 1
            return [str(_) for _ in range(1, 10) if used[_] == 0]

        def dfs(pos: int) -> bool:
            if pos == 81:
                return True
            x, y = divmod(pos, 9)
            if board[x][y] != '.':
                return dfs(pos + 1)
            for num in get_options(x, y):
                board[x][y] = num
                if dfs(pos + 1):
                    return True
                else:
                    board[x][y] = '.'
            return False

        dfs(0)

    def solve_sudoku2(self, board: List[List[str]]) -> None:
        def dfs(pos: int) -> bool:
            if pos == 81:
                return True
            row, col = divmod(pos, 9)
            blk = row // 3 * 3 + col // 3
            if board[row][col] != '.':
                return dfs(pos + 1)
            for num in range(1, 10):
                if row_candidates[row][num] and col_candidates[col][num] and blk_candidates[blk][num]:
                    board[row][col] = str(num)
                    row_candidates[row][num] = col_candidates[col][num] = blk_candidates[blk][num] = False
                    if dfs(pos + 1):
                        return True
                    else:
                        board[row][col] = '.'
                        row_candidates[row][num] = col_candidates[col][num] = blk_candidates[blk][num] = True
            return False

        row_candidates = [([False] + [True] * 9) for _ in range(9)]
        col_candidates = [([False] + [True] * 9) for _ in range(9)]
        blk_candidates = [([False] + [True] * 9) for _ in range(9)]
        for row in range(9):
            for v in board[row]:
                if v != '.':
                    row_candidates[row][int(v)] = False
        for col in range(9):
            for row in range(9):
                if board[row][col] != '.':
                    col_candidates[col][int(board[row][col])] = False
        for blk in range(9):
            x, y = divmod(blk, 3)
            for row in range(x * 3, x * 3 + 3):
                for col in range(y * 3, y * 3 + 3):
                    if board[row][col] != '.':
                        blk_candidates[blk][int(board[row][col])] = False
        dfs(0)
