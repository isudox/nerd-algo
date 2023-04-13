"""289. Game of Life
https://leetcode.com/problems/game-of-life/

According to the Wikipedia's article: "The Game of Life, also known simply as
Life, is a cellular automaton devised by
the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1)
or dead (0). Each cell interacts with its eight neighbors (horizontal,
vertical, diagonal) using the following four rules (taken from the above
Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every
cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle,
the board is infinite, which would cause problems when the active area
encroaches the border of the array. How would you address these problems?
"""
from typing import List


class Solution:
    def game_of_life(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def count(x: int, y: int) -> int:
            summary = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < rows and 0 <= j < cols:
                        summary += board[i][j]
            return summary - board[x][y]

        rows, cols = len(board), len(board[0])
        store = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                store[i][j] = count(i, j)
        for i in range(rows):
            for j in range(cols):
                condition = store[i][j]
                if board[i][j] == 1:
                    if condition < 2 or condition > 3:
                        board[i][j] = 0
                else:
                    if condition == 3:
                        board[i][j] = 1
