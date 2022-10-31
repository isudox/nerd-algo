package com.leetcode;

/**
 * 766. Toeplitz Matrix
 * https://leetcode.com/problems/toeplitz-matrix/
 */
public class Problem766 {
    public boolean isToeplitzMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        for (int i = 0; i < n; i++) {
            int x = 0, y = i;
            int num = matrix[x][y];
            while (x < m && y < n) {
                if (matrix[x++][y++] != num) {
                    return false;
                }
            }
        }
        for (int i = m - 1; i > 0; i--) {
            int x = i, y = 0;
            int num = matrix[x][y];
            while (x < m && y < n) {
                if (matrix[x++][y++] != num) {
                    return false;
                }
            }
        }
        return true;
    }
}
