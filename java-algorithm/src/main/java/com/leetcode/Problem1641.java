package com.leetcode;

/**
 * 1641. Count Sorted Vowel Strings
 * https://leetcode.com/problems/count-sorted-vowel-strings/
 */
public class Problem1641 {
    public int countVowelStrings(int n) {
        return dfs(0, n, new int[5][n + 1]);
    }

    private int dfs(int start, int n, int[][] memo) {
        if (n == 1) {
            return 5 - start;
        }
        if (memo[start][n] > 0) {
            return memo[start][n];
        }
        int ret = 0;
        for (int i = start; i < 5; i++) {
            ret += dfs(i, n - 1, memo);
        }
        return memo[start][n] = ret;
    }

    public int countVowelStrings1(int n) {
        int[][] dp = new int[5][n + 1];  // dp[i][j]: start with chars[i] to build j len string
        for (int i = 0; i < 5; i++) {
            dp[i][1] = 5 - i;
        }

        for (int i = 4; i >= 0; i--) {
            for (int j = 1; j <= n; j++) {
                if (j == 1) {
                    dp[i][j] = 5 - i;
                } else {
                    dp[i][j] += dp[i][j - 1];
                }
            }
        }
        return dp[0][n];
    }
}
