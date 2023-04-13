"""794. Valid Tic-Tac-Toe State
https://leetcode.com/problems/valid-tic-tac-toe-state/
"""
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def has_winner(p: str) -> bool:
            return any(board[i][0] == p and board[i][1] == p and board[i][2] == p or
                board[0][i] == p and board[1][i] == p and board[2][i] == p for i
                in range(3)) or \
            board[0][0] == p and board[1][1] == p and board[2][2] == p or \
            board[0][2] == p and board[1][1] == p and board[2][0] == p

        cnt = {'X': 0, 'O': 0, ' ': 0}
        for row in board:
            for ch in row:
                cnt[ch] += 1
        if cnt['X'] != cnt['O'] and cnt['X'] != cnt['O'] + 1:
            return False
        if has_winner('X') and cnt['X'] != cnt['O'] + 1:
            return False
        if has_winner('O') and cnt['X'] != cnt['O']:
            return False
        return True
