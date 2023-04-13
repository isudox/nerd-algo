package com.leetcode;

/**
 * 1155. Number of Dice Rolls With Target Sum
 * https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
 */
public class Problem1155 {
    public int numRollsToTarget(int n, int k, int target) {
        if (k * n < target || n > target) {
            return 0;
        }
        int base = (int) 1e9 + 7;
        int[][] dp = new int[n + 1][target + 1];
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = i; j <= target; j++) {
                for (int x = 1; x <= k; x++) {
                    if (j >= x) {
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % base;
                    }
                }
            }
        }
        return dp[n][target];
    }
}
