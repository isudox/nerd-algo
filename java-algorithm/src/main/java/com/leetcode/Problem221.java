package com.leetcode;

/**
 * 221. Maximal Square
 * https://leetcode.com/problems/maximal-square/
 */
public class Problem221 {

    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dp = new int[m][n];
        int max = 0;
        for (int i = 0; i < n; i++) {
            if (matrix[0][i] == '1') {
                dp[0][i] = 1;
                max = 1;
            }
        }
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == '1') {
                dp[i][0] = 1;
                max = 1;
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == '0') {
                    dp[i][j] = 0;
                } else if (dp[i - 1][j - 1] == 0) {
                    dp[i][j] = 1;
                } else {
                    int ret = helper(matrix, i, j);
                    if (ret > dp[i - 1][j - 1]) {
                        dp[i][j] = dp[i - 1][j - 1] + 1;
                    } else {
                        dp[i][j] = ret;
                    }
                }
                max = Math.max(max, dp[i][j]);
            }
        }
        return max * max;
    }

    private int helper(char[][] matrix, int x, int y) {
        int a = 0, b = 0;
        for (int i = y; i >= 0; i--) {
            if (matrix[x][i] == '0') {
                break;
            }
            a++;
        }
        for (int i = x; i >= 0; i--) {
            if (matrix[i][y] == '0') {
                break;
            }
            b++;
        }
        return Math.min(a, b);
    }
}
