package com.leetcode;

/**
 * 867. Transpose Matrix
 * https://leetcode.com/problems/transpose-matrix/
 */
public class Problem867 {
    public int[][] transpose(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int[][] ans = new int[n][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans[j][i] = matrix[i][j];
            }
        }
        return ans;
    }
}
