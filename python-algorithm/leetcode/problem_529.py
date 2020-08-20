"""529. Minesweeper
https://leetcode.com/problems/minesweeper/
"""
from typing import List


class Solution:
    def update_board(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(x: int, y: int):
            mine_count = 0
            for d in dirs:
                new_x, new_y = x + d[0], y + d[1]
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if board[new_x][new_y] == 'M':
                        mine_count += 1
            if mine_count > 0:
                board[x][y] = str(mine_count)
                return
            board[x][y] = 'B'
            for d in dirs:
                new_x, new_y = x + d[0], y + d[1]
                if 0 <= new_x < rows and 0 <= new_y < cols and board[new_x][new_y] != 'B':
                    dfs(new_x, new_y)

        rows, cols = len(board), len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [-1, -1], [1, 1], [1, -1]]
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            dfs(x, y)
        return board

if __name__ == '__main__':
    sol = Solution()
    board = [['B', '1', 'E', '1', 'B'],['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    click = [1,2]
    print(sol.update_board(board, click))
