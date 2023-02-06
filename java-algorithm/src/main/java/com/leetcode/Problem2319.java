package com.leetcode;


/**
 * 2319. Check if Matrix Is X-Matrix
 * https://leetcode.com/problems/check-if-matrix-is-x-matrix
 */
class Problem2319 {
    public boolean checkXMatrix(int[][] grid) {
        int m = grid.length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                if ((i == j || i + j == m - 1)) {
                    if (grid[i][j] == 0) {
                        return false;
                    }
                } else if (grid[i][j] != 0) {
                    return false;
                }
            }
        }
        return true;
    }
}
