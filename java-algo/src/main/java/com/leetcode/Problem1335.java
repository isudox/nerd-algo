package com.leetcode;

import java.util.Arrays;

/**
 * 1335. Minimum Difficulty of a Job Schedule
 * https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
 */
public class Problem1335 {
    public int minDifficulty(int[] jobDifficulty, int d) {
        int n = jobDifficulty.length;
        if (n < d) {
            return -1;
        }
        int[][] maxDifficulty = new int[n][n]; // 预计算从第 i 到第 j 项工作的最大难度
        for (int i = 0; i < n; i++) {
            maxDifficulty[i][i] = jobDifficulty[i];
            for (int j = i + 1; j < n; j++) {
                maxDifficulty[i][j] = Math.max(maxDifficulty[i][j - 1], jobDifficulty[j]);
            }
        }
        int[][] dp = new int[n][d + 1]; // dp[i][j] 表示截止到第 i 项工作，耗时 j 天的总难度
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], -1);
        }
        for (int i = 0; i < n; i++) {
            dp[i][1] = maxDifficulty[0][i];
            for (int j = 2; j <= Math.min(d, i + 1); j++) {
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = 0; k < i; k++) {
                    if (dp[k][j - 1] > -1) {
                        // dp[i][j] = dp[k][j - 1] + max_difficulty[k+1][j]
                        dp[i][j] = Math.min(dp[i][j], dp[k][j - 1] + maxDifficulty[k + 1][i]);
                    }
                }
            }
        }
        return dp[n - 1][d];
    }
}
