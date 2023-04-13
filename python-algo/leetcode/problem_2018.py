"""2018. Check if Word Can Be Placed In Crossword
https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/
"""
from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def check(pos: int, lo: int, hi: int, mode: bool) -> bool:
            valid = True
            for i in range(lo, hi):
                if mode:  # row mode
                    val = board[pos][i]
                else:
                    val = board[i][pos]
                if val == ' ' or val == word[i - lo]:
                    continue
                valid = False
            if valid:
                return True
            for i in range(lo, hi):
                if mode:  # row mode
                    val = board[pos][i]
                else:
                    val = board[i][pos]
                if val == ' ' or val == reverse_word[i - lo]:
                    continue
                return False
            return True

        m, n, size = len(board), len(board[0]), len(word),
        reverse_word = word[::-1]
        if size > max(m, n):
            return False
        for r, row in enumerate(board):
            if n < size:
                break
            start = -1
            for i in range(n):
                if row[i] == '#':
                    if i - 1 - start == size and check(r, start + 1, i, True):
                        return True
                    start = i
                elif i == n - 1:
                    if i - start == size and check(r, start + 1, i + 1, True):
                        return True
                    start = i
        for j in range(n):
            if m < size:
                break
            start = -1
            for i in range(m):
                if board[i][j] == '#':
                    if i - 1 - start == size and check(j, start + 1, i, False):
                        return True
                    start = i
                elif i == m - 1:
                    if i - start == size and check(j, start + 1, i + 1, False):
                        return True
                    start = i
        return False
