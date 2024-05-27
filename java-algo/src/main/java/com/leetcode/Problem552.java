package com.leetcode;

/**
 * 552. Student Attendance Record II
 * https://leetcode.com/problems/student-attendance-record-ii/
 */
public class Problem552 {
    public int checkRecord(int n) {
        int base = (int) 1e9 + 7;
        int[][][] dp = new int[n + 1][2][3];
        dp[0][0][0] = 1;
        for (int i = 1; i <= n; i++) {
            // be preset
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 3; k++) {
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % base;
                }
            }
            // be absent
            for (int j = 0; j < 3; j++) {
                dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][j]) % base;
            }
            // be late
            for (int j = 0; j < 2; j++) {
                for (int k = 1; k < 3; k++) {
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % base;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) {
                ans = (ans + dp[n][i][j]) % base;
            }
        }
        return ans;
    }
}
