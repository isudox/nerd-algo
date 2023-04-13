package com.leetcode;

/**
 * 329. Longest Increasing Path in a Matrix
 * https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
 *
 * Given an integer matrix, find the length of the longest increasing path.
 *
 * From each cell, you can either move to four directions: left, right, up or down.
 * You may NOT move diagonally or move outside of the boundary
 * (i.e. wrap-around is not allowed).
 *
 * Example 1:
 *
 * Input: nums =
 * [
 *   [9,9,4],
 *   [6,6,8],
 *   [2,1,1]
 * ]
 * Output: 4
 * Explanation: The longest increasing path is [1, 2, 6, 9].
 *
 * Example 2:
 *
 * Input: nums =
 * [
 *   [3,4,5],
 *   [3,2,6],
 *   [2,2,1]
 * ]
 * Output: 4
 * Explanation: The longest increasing path is [3, 4, 5, 6].
 * Moving diagonally is not allowed.
 */
public class Problem329 {

    private static final int[][] DIRS = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int longestIncreasingPath(int[][] matrix) {
        if (null == matrix || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int rows = matrix.length, cols = matrix[0].length;
        int[][] memo = new int[rows][cols];
        int ans = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int ret = dfs(i, j, matrix, memo);
                if (ret > ans) {
                    ans = ret;
                }
            }
        }
        return ans;
    }

    private int dfs(int x, int y, int[][] matrix, int[][] memo) {
        if (memo[x][y] != 0)
            return memo[x][y];
        int ret = 1;
        for (int[] d : DIRS) {
            int nx = x + d[0], ny = y + d[1];
            if (0 <= nx && nx < matrix.length && 0 <= ny && ny < matrix[0].length && matrix[nx][ny] > matrix[x][y]) {
                ret = Math.max(ret, 1 + dfs(nx, ny, matrix, memo));
            }
        }
        return memo[x][y] = ret;
    }
}
