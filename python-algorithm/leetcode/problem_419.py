"""419. Battleships in a Board
https://leetcode.com/problems/battleships-in-a-board/
"""
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def helper(r: int, c: int):
            found = False
            board[r][c] = '.'
            for dr, dc in ([0, 1], [1, 0]):
                if found:
                    return
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'X':
                    found = True
                    helper(nr, nc)

        ans = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    helper(i, j)
                    ans += 1
        return ans
