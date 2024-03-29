package com.leetcode;

/**
 * 59. Spiral Matrix II
 * https://leetcode.com/problems/spiral-matrix-ii/
 */
public class Problem59 {
    public int[][] generateMatrix(int n) {
        int m = n * n;
        int[][] ans = new int[n][n];
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // right, down, left, up
        int r = 0, c = 0, x = 0;
        for (int i = 1; i <= m; i++) {
            ans[r][c] = i;
            int nr = r + dirs[x][0], nc = c + dirs[x][1];
            if (0 <= nr && nr < n && 0 <= nc && nc < n && ans[nr][nc] == 0) {
                r = nr;
                c = nc;
            } else {
                x = (x + 1) % 4;
                r += dirs[x][0];
                c += dirs[x][1];
            }
        }
        return ans;
    }
}
