package com.leetcode;

/**
 * 980. Unique Paths III
 * https://leetcode.com/problems/unique-paths-iii/
 * <p>
 * On a 2-dimensional grid, there are 4 types of squares:
 * <ul>
 * <li>1 represents the starting square.  There is exactly one starting square.</li>
 * <li>2 represents the ending square.  There is exactly one ending square.</li>
 * <li>0 represents empty squares we can walk over.</li>
 * <li>-1 represents obstacles that we cannot walk over.</li>
 * </ul>
 * Return the number of 4-directional walks from the starting square to the
 * ending square, that walk over every non-obstacle square exactly once.
 * <p>
 * Example 1:
 * <p>
 * Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
 * Output: 2
 * Explanation: We have the following two paths:
 * 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
 * 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
 * <p>
 * Note:
 * <p>
 * 1 <= grid.length * grid[0].length <= 20
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
