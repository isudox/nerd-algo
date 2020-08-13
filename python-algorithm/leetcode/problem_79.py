"""79. Word Search
https://leetcode.com/problems/word-search/description/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

Example:

board =
[
⁠ ['A','B','C','E'],
⁠ ['S','F','C','S'],
⁠ ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, length = len(board), len(board[0]), len(word)
        # mark the element in board
        usable = [[True] * cols for _ in range(rows)]
        # four directions
        d = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def backtrack(r: int, c: int, i: int) -> bool:
            """
            backtrack checking the character
            :param r: the index of row
            :param c: the index of col
            :param i: the index of character
            :return:
            """
            if i == length:
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[i]:
                return False
            if not usable[r][c]:
                return False

            usable[r][c] = False
            if any(backtrack(r + x[0], c + x[1], i + 1) for x in d):
                return True
            usable[r][c] = True
            return False

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False
