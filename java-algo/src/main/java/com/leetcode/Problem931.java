package com.leetcode;

/**
 * 931. Minimum Falling Path Sum
 * https://leetcode.com/problems/minimum-falling-path-sum/
 */
public class Problem931 {
    public int minFallingPathSum(int[][] matrix) {
        int ans = 9999999;
        int n = matrix.length;
        int[] dp0 = new int[n], dp1 = new int[n];
        System.arraycopy(matrix[0], 0, dp0, 0, n);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp1[j] = dp0[j] + matrix[i][j];
                if (j > 0) {
                    dp1[j] = Math.min(dp1[j], dp0[j - 1] + matrix[i][j]);
                }
                if (j < n - 1) {
                    dp1[j] = Math.min(dp1[j], dp0[j + 1] + matrix[i][j]);
                }
            }
            System.arraycopy(dp1, 0, dp0, 0, n);
        }
        for (int num : dp0) {
            ans = Math.min(ans, num);
        }
        return ans;
    }
}
