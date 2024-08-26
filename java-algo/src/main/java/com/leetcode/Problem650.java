package com.leetcode;

import java.util.Arrays;

/**
 * 650. 2 Keys Keyboard
 * https://leetcode.com/problems/2-keys-keyboard
 */
public class Problem650 {
    public int minSteps(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, 1001);
        dp[1] = 0;
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= i / 2; j++) {
                if (i % j == 0) {
                    dp[i] = Math.min(dp[i], dp[j] + i / j);
                }
            }
        }
        return dp[n];
    }
}
