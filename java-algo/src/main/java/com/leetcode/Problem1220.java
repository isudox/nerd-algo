package com.leetcode;

import java.util.Arrays;

public class Problem1220 {
    public int countVowelPermutation(int n) {
        int base = (int) (1e9 + 7);
        long[][] dp = new long[n + 1][5];
        Arrays.fill(dp[1], 1);
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < 5; j++) {
                if (j == 0) {
                    // 'ea', 'ia', 'ua'
                    dp[i][j] += dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4];
                }
                if (j == 1) {
                    // 'ae', 'ie'
                    dp[i][j] += dp[i - 1][0] + dp[i - 1][2];
                }
                if (j == 2) {
                    // 'ei', 'oi'
                    dp[i][j] += dp[i - 1][1] + dp[i - 1][3];
                }
                if (j == 3) {
                    // 'io'
                    dp[i][j] += dp[i - 1][2];
                }
                if (j == 4) {
                    // 'iu', 'ou'
                    dp[i][j] += dp[i - 1][2] + dp[i - 1][3];
                }
                dp[i][j] %= base;
            }
        }
        long ans = 0;
        for (long num : dp[n]) {
            ans += num;
        }
        return (int) (ans % base);
    }
}
