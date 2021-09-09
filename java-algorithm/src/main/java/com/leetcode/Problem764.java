package com.leetcode;

/**
 * 764. Largest Plus Sign
 * https://leetcode.com/problems/largest-plus-sign/
 */
public class Problem764 {

    static final int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int orderOfLargestPlusSign(int n, int[][] mines) {
        int ans = 0;
        int[][][] memo = new int[n][n][4];
        int[][] matrix = new int[n][n];
        for (int[] mine : mines) {
            matrix[mine[0]][mine[1]] = -1;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ans = Math.max(ans, helper(i, j, n, memo, matrix));
            }
        }
        return ans;
    }

    private int helper(int x, int y, int n, int[][][] memo, int[][] matrix) {
        int cnt = n;
        for (int d = 0; d < 4; d++) {
            cnt = Math.min(cnt, dfs(x, y, d, n, memo, matrix));
        }
        return cnt;
    }

    private int dfs(int x, int y, int d, int n, int[][][] memo, int[][] matrix) {
        if (matrix[x][y] == -1) {
            return 0;
        }
        if (memo[x][y][d] != 0) {
            return memo[x][y][d];
        }
        int nx = x + moves[d][0], ny = y + moves[d][1];
        int ret = 1;
        if (0 <= nx && nx < n && 0 <= ny && ny < n) {
            ret += dfs(nx, ny, d, n, memo, matrix);
        }
        return memo[x][y][d] = ret;
    }
}
