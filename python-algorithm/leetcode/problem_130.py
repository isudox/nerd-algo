"""130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O),
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on
the border of the board are not flipped to 'X'. Any 'O' that is not on the
border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_border(x: int, y: int) -> bool:
            nonlocal rows, cols
            return x == 0 or x == rows - 1 or y == 0 or y == cols - 1

        def is_adjacent(x: int, y: int):
            nonlocal rows, cols
            for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= x + d[0] < rows and 0 <= y + d[1] < cols \
                    and not mark[x + d[0]][y + d[1]] \
                    and board[x + d[0]][y + d[1]] == 'O':
                    mark[x + d[0]][y + d[1]] = True
                    is_adjacent(x + d[0], y + d[1])

        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        mark = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if is_border(i, j) and board[i][j] == 'O':
                    mark[i][j] = True
                    is_adjacent(i, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and not mark[i][j]:
                    board[i][j] = 'X'
