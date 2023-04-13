package com.leetcode;

/**
 * 289. Game of Life
 * https://leetcode.com/problems/game-of-life/
 */
public class Problem289 {
    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                helper(board, i, j);
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == -1) {
                    board[i][j] = 0;
                } else if (board[i][j] == -2) {
                    board[i][j] = 1;
                }
            }
        }
    }

    private void helper(int[][] board, int x, int y) {
        int m = board.length, n = board[0].length;
        int cnt1 = 0;
        for (int i = x - 1; i <= x + 1; i++) {
            for (int j = y - 1; j <= y + 1; j++) {
                if (0 <= i && i < m && 0 <= j && j < n) {
                    if (i == x && j == y) {
                        continue;
                    }
                    int val = board[i][j];
                    if (val == 1 || val == -1) {
                        cnt1++;
                    }
                    if (cnt1 > 3) {
                        break;
                    }
                }
            }
        }
        if (board[x][y] == 1) {
            if (cnt1 < 2 || cnt1 > 3) {
                board[x][y] = -1;  // -1: alive -> die
            }
        } else {
            if (cnt1 == 3) {
                board[x][y] = -2; // -2: die -> alive
            }
        }
    }
}
