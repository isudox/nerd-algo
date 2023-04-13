package com.leetcode;

import java.util.Arrays;

/**
 * 629. K Inverse Pairs Array
 * https://leetcode.com/problems/k-inverse-pairs-array/
 */
public class Problem629 {
    public int kInversePairs(int n, int k) {
        int mod = (int) 1e9 + 7;
        int[][] dp = new int[n + 1][k + 1];
        int[][] sum = new int[n + 1][k + 1];
        dp[1][0] = 1;
        Arrays.fill(sum[1], 1);
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                if (j < i) {
                    dp[i][j] = sum[i - 1][j];
                } else {
                    dp[i][j] = (sum[i - 1][j] - sum[i - 1][j - i] + mod) % mod;
                }
                if (j == 0) {
                    sum[i][j] = dp[i][j];
                } else {
                    sum[i][j] = (sum[i][j - 1] + dp[i][j]) % mod;
                }
            }
        }
        return dp[n][k];
    }
}
