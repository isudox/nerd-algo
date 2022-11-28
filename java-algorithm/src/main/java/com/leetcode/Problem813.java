package com.leetcode;

/**
 * 813. Largest Sum of Averages
 * https://leetcode.com/problems/largest-sum-of-averages/
 */
public class Problem813 {
    public double largestSumOfAverages(int[] nums, int k) {
        int n = nums.length;
        double[] sums = new double[n + 1];
        for (int i = 1; i <= n; i++) {
            sums[i] = sums[i - 1] + nums[i - 1];
        }
        double[][] dp = new double[n + 1][k + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= Math.min(i, k); j++) {
                if (j == 1) {
                    dp[i][1] = sums[i] / i;
                } else {
                    for (int x = 2; x <= i; x++) {
                        dp[i][j] = Math.max(dp[i][j], dp[x - 1][j - 1] + (sums[i] - sums[x - 1]) / (i - x + 1));
                    }
                }
            }
        }
        return dp[n][k];
    }
}
