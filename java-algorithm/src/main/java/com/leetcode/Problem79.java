package com.leetcode;

/**
 * 79. Word Search
 * https://leetcode.com/problems/word-search/
 */
public class Problem79 {
    private static final int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    private char[][] board;
    private String word;
    private int m;
    private int n;

    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.word = word;
        this.m = board.length;
        this.n = board[0].length;
        boolean[][] visited = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word.charAt(0) && backtrack(visited, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean backtrack(boolean[][] visited, int x, int y, int i) {
        if (i == word.length() - 1) {
            return true;
        }
        visited[x][y] = true;
        for (int[] d : dirs) {
            int nx = x + d[0], ny = y + d[1];
            if (0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny] && board[nx][ny] == word.charAt(i + 1)) {
                if (backtrack(visited, nx, ny, i + 1)) {
                    return true;
                }
            }
        }
        visited[x][y] = false;
        return false;
    }
}
