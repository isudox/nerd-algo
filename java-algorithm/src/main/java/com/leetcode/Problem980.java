package com.leetcode;

/**
 * 980. Unique Paths III
 * https://leetcode.com/problems/unique-paths-iii/
 */
public class Problem980 {

    private int zeros;
    private int ans;

    public int uniquePathsIII(int[][] grid) {
        int startX = 0, startY = 0;
        int lines = grid.length, columns = grid[0].length;
        for (int i = 0; i < lines; i++) {
            for (int j = 0; j < columns; j++) {
                if (grid[i][j] == 0) {
                    this.zeros++;
                }
                if (grid[i][j] == 1) {
                    startX = i;
                    startY = j;
                }
            }
        }
        boolean[][] visited = new boolean[lines][columns];
        visited[startX][startY] = true;
        backtrack(grid, visited, startX, startY, 0);
        return this.ans;
    }

    private void backtrack(int[][] grid, boolean[][] visited, int i, int j, int count) {
        int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int[] move : moves) {
            move[0] += i;
            move[1] += j;
            if (move[0] >= 0 && move[0] < grid.length && move[1] >= 0 && move[1] < grid[0].length && !visited[move[0]][move[1]] && grid[move[0]][move[1]] != -1) {
                if (grid[move[0]][move[1]] == 0) {
                    visited[move[0]][move[1]] = true;
                    backtrack(grid, visited, move[0], move[1], count + 1);
                    visited[move[0]][move[1]] = false;
                } else if (count == this.zeros) {
                    this.ans++;
                }
            }
        }
    }
}
