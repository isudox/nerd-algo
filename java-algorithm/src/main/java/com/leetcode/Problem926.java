package com.leetcode;

/**
 * 926. Flip String to Monotone Increasing
 * https://leetcode.com/problems/flip-string-to-monotone-increasing/
 */
public class Problem926 {
    public int minFlipsMonoIncr(String s) {
        int n = s.length();
        int[][] dp = new int[n][2];
        if (s.charAt(n - 1) == '0') {
            dp[n - 1][1] = 1;
        } else {
            dp[n - 1][0] = 1;
        }
        for (int i = n - 2; i >= 0; i--) {
            if (s.charAt(i) == '0') {
                dp[i][0] = Math.min(dp[i + 1][0], dp[i + 1][1]);
                dp[i][1] = dp[i + 1][1] + 1;
            } else {
                dp[i][0] = Math.min(dp[i + 1][0], dp[i + 1][1]) + 1;
                dp[i][1] = dp[i + 1][1];
            }
        }
        return Math.min(dp[0][0], dp[0][1]);
    }
}
