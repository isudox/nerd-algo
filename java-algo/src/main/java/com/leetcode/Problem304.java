package com.leetcode;

/**
 * 304. Range Sum Query 2D - Immutable
 * https://leetcode.com/problems/range-sum-query-2d-immutable/
 */
public class Problem304 {
    private static class NumMatrix {
        private int[][] preSums;

        public NumMatrix(int[][] matrix) {
            int m = matrix.length, n = matrix[0].length;
            preSums = new int[m][n];
            preSums[0][0] = matrix[0][0];
            for (int i = 1; i < n; i++) {
                preSums[0][i] = preSums[0][i - 1] + matrix[0][i];
            }
            for (int i = 1; i < m; i++) {
                preSums[i][0] = preSums[i - 1][0] + matrix[i][0];
                for (int j = 1; j < n; j++) {
                    preSums[i][j] = preSums[i - 1][j] + preSums[i][j - 1] + matrix[i][j] - preSums[i - 1][j - 1];
                }
            }
        }

        public int sumRegion(int row1, int col1, int row2, int col2) {
            int a = preSums[row2][col2];
            int b = row1 > 0 && col1 > 0 ? preSums[row1 - 1][col1 - 1] : 0;
            int c = row1 > 0 ? preSums[row1 - 1][col2] : 0;
            int d = col1 > 0 ? preSums[row2][col1 - 1] : 0;
            return a + b - c - d;
        }
    }
}
